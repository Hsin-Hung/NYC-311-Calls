# Big-Data-Project

## Install Dependencies
```sh
pip install -r requirements.txt
```
## API Configurations

To set up the necessary api configuration, follow the steps below:

1. [Sign Up for an App Token](https://dev.socrata.com/foundry/data.cityofnewyork.us/erm2-nwe9#:~:text=on%20API%20changes-,App%20Tokens,-All%20requests%20should)
   
2. Create an .env File

    Create a file named `.env` in the root of the project. You can use the following command to create the file:
    
    ```bash
    touch .env
    ```

3. Add App Token Information

    Add the following content to `.env`, replacing the placeholders `<token>` with your actual app token:
    
    ```yaml
    APP_TOKEN=<token>
    ```