# Streamlit Alliander

This repository is meant to be a guideline to create basic visuals in streamlit about MRID'S. 

## Preperation

Use the package manager [pip](https://pypi.org/project/streamlit/) to install streamlit.

```bash
pip install streamlit
```

The requirements.txt and st_page.py are used to run streamlit.

## Usage
Within the st_page.py we've used all of the other data resources to visualize them within the streamlit page.

It's worth noting that we've created a website for the map on the second streamlit page with the following code:
```python
if selected == "Map":
    components.iframe("https://lemon-smoke-0c2fad103.2.azurestaticapps.net/",height= 800)
```
This website will be offline sooner or later due to hosting fee's.
However, might it be of your best intrest to create the static web page, we kindly ask you to visit [the index_html repository](https://github.com/DinandK/index_html)
