from setuptools import setup
from setuptools import find_packages

setup(
    name="ChatDoctor_assistant",
    version="0.1.0",
    author="NGÔ VĂN ÚC",
    author_email="ngovanuc.1508@gmail.com",
    description="ChatDoctor_assistant is a Python package that provides a chatbot interface for medical inquiries and assistance. It utilizes the OpenAI API to generate responses based on user input and offers features such as conversation history, file upload, and text-to-speech functionality.",
    long_description=open("README.md").read(),          # Mô tả dài, dùng README
    long_description_content_type="text/markdown",      # Định dạng mô tả dài
    url="https://github.com/ngovanuc/ChatDoctor_assistant",
    packages=find_packages(),                           # Tìm tất cả các package trong thư mục hiện tại
    install_requires=[

    ],
    classifiers=[       # Các phân loại cho package
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',                            # Phiên bản Python yêu cầu

)