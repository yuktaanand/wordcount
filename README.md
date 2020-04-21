This is just a simple Django Project to get through the working of Django

Step1: Ensure pip is up To Date
    Windows
        py -m pip --version
        pip 9.0.1 from c:\python36\lib\site-packages (Python 3.6.1)

        You can make sure that pip is up-to-date by running:
        py -m pip install --upgrade pip

    Linux and macOS
        python3 -m pip install --user --upgrade pip

        Afterwards, you should have the newest pip installed in your user site:
        python3 -m pip --version
        pip 9.0.1 from $HOME/.local/lib/python3.6/site-packages (python 3.6)
    
Step2: Installing virtualenv 
    On Windows:
        py -m pip install --user virtualenv

    On macOS and Linux:
        python3 -m pip install --user virtualenv

Step3: Creating a virtual environment
    On Windows:
        py -m venv env

    On macOS and Linux:
        python3 -m venv env

Step4: Activating a virtual environment
    On Windows:
        .\env\Scripts\activate

    On macOS and Linux:
        source env/bin/activate

Step5: pip install -r requirements.txt

