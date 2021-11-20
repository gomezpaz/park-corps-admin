"""
This file is the framework for generating multiple Streamlit applications 
through an object oriented framework. 
"""

# Import necessary libraries
import streamlit as st
import pandas as pd
import numpy as np

# Define the multipage class to manage the multiple apps in our program


class MultiPage:
    """Framework for combining multiple streamlit applications."""

    def __init__(self) -> None:
        """Constructor class to generate a list which will store all our applications as an instance variable."""
        self.pages = []
        self.parking_spaces_master = pd.DataFrame(np.random.randn(
            10, 5), columns=('col %d' % i for i in range(5)))

    def add_page(self, title, func) -> None:
        """Class Method to Add pages to the project
        Args:
            title ([str]): The title of page which we are adding to the list of apps 

            func: Python function to render this page in Streamlit
        """

        self.pages.append(
            {
                "title": title,
                "function": func(self)
            }
        )

    def run(self):
        # Drodown to select the page to run
        page = st.sidebar.selectbox(
            'App Navigation',
            self.pages,
            format_func=lambda page: page['title']
        )

        # run the app function
        page['function']()
