import pandas as pd
from google import genai
from google.genai import types
import io
import sys
import base64
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

class GeminiAgent:
    def __init__(self, project_id, location, dataset_path):
        self.project_id = project_id
        self.location = location
        self.dataset_path = dataset_path
        self.df = pd.read_csv(dataset_path)
        
        # Initialize Google GenAI Client
        self.client = genai.Client(
            vertexai=True,
            project=project_id,
            location=location
        )
        
        # Using Gemini 2.0 Flash (Experimental) as requested
        self.model_name = "gemini-2.0-flash-exp" 

    def get_dataset_info(self):
        buffer = io.StringIO()
        self.df.info(buf=buffer)
        info_str = buffer.getvalue()
        head_str = self.df.head().to_markdown()
        return f"Dataset Info:\n{info_str}\n\nFirst 5 rows:\n{head_str}"

    def generate_response(self, user_query):
        dataset_context = self.get_dataset_info()
        
        prompt = f"""
You are a data analysis assistant. You have access to a pandas DataFrame named `df`.
The dataset contains information about education and economic growth.

Here is the dataset schema and sample data:
{dataset_context}

User Query: {user_query}

Please generate Python code to answer the user's query. 
- The code should use `pandas`, `matplotlib`, or `seaborn`.
- Assume the dataframe `df` is already loaded.
- If the user asks for a plot, create it using matplotlib/seaborn. 
- **IMPORTANT**: To display the plot in the UI, save the plot to a BytesIO object and encode it to base64. 
- Assign the base64 string to a variable named `plot_base64`.
- If there is a text answer, print it to stdout.
- Do not use `plt.show()`.
- Wrap the code in a markdown code block like ```python ... ```.
- Only provide the code, no explanation is needed before or after.
"""
        
        contents = [
            types.Content(
                role="user",
                parts=[
                    types.Part.from_text(text=prompt)
                ]
            )
        ]
        
        generate_content_config = types.GenerateContentConfig(
            temperature = 0.2, # Lower temperature for code generation
            top_p = 0.95,
            max_output_tokens = 8192,
            response_mime_type = "text/plain",
        )

        response = self.client.models.generate_content(
            model = self.model_name,
            contents = contents,
            config = generate_content_config,
        )
        
        return response.text

    def execute_code(self, code_str):
        # Clean up code block markers
        code_str = code_str.strip()
        if code_str.startswith("```python"):
            code_str = code_str[9:]
        if code_str.startswith("```"):
            code_str = code_str[3:]
        if code_str.endswith("```"):
            code_str = code_str[:-3]
            
        # Capture stdout
        old_stdout = sys.stdout
        redirected_output = io.StringIO()
        sys.stdout = redirected_output
        
        local_vars = {'df': self.df, 'pd': pd, 'plt': plt, 'base64': base64, 'io': io}
        
        plot_base64 = None
        
        try:
            exec(code_str, {}, local_vars)
            output = redirected_output.getvalue()
            if 'plot_base64' in local_vars:
                plot_base64 = local_vars['plot_base64']
        except Exception as e:
            output = f"Error executing code: {e}"
        finally:
            sys.stdout = old_stdout
            
        return output, plot_base64
