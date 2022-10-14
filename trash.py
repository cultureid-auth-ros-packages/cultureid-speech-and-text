rasa:
    build:
      context: ./
      dockerfile: Dockerfile_rasa
    ports:
    - "5005:5005"
    volumes:
    - ".:/app/"   #gia na parei ta arxeia kai to model
    command: train --domain domain.yml --data data --out models


 


  # callback-server:
  #   build:
  #     context: ./
  #     dockerfile: Dockerfile_callback

  #   volumes:
  #   - ".:/app/"

    # command: python3 callback_server.py
