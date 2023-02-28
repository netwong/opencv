import streamlit as st
import mediapipe as mp
import cv2
import numpy as np
import tempfile
import time
from PIL import Image

st.title('Face Mesh App using MediaPipe')
st.markdown(
  """ 
  <style>
  [data-testid="stSidebar"][aria-expanded="true"] > div:first-child{
    width: 350px
  }
  [data-testid="stSidebar"][aria-expanded="false"] > div:first-child{
    width: 350px
    margin-left: -350px
  }
  """
)
