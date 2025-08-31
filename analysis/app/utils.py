import re 
  

  def clean_text(text):
        text = text.lower()
       text = re.sub(r'[^a-z0-9\s]', '', text)
       return text