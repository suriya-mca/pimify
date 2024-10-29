# pimify
Pimify is an open-source Product Information Management (PIM) platform

![image](https://github.com/user-attachments/assets/8dc2a7b5-3c45-4bdf-a0fa-b9dd625ea2ad)

## Quick Installation with Script

You can set up the project quickly by running the installation script. Make sure you have the necessary permissions.

### Prerequisites

Ensure the following is installed on your system:

- **Python** (version 3.7 or higher)
- **PostgreSQL** (make sure the PostgreSQL server is running and accessible)

### Clone the project

```bash
  git clone https://github.com/suriya-mca/pimify.git
```

### Go to the project directory

```bash
  cd pimify
```

### Create .env file

```bash
  SECRET_KEY = secret_key
  DEBUG = True
  NAME = db_name
  USER = postgres
  PASSWORD = password
  HOST = localhost
  PORT = 5432
```

### On Mac/Linux

```bash
  chmod +x install.sh
  ./install.sh
```

### On Windows

```bash
  ./install.bat
```

## Contributing

Contributions make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**. See [CONTRIBUTING.md](./CONTRIBUTING.md) for more details on how to contribute.

1. Fork this repository to your GitHub account
2. Clone the forked repository to your local machine
3. Create your Feature or Fix Branch (`git checkout -b feature/AmazingFeature`)
4. Make your changes and ensure they are properly tested
5. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
6. Push to the Branch (`git push origin feature/AmazingFeature`)
7. Open a Pull Request

## License

Distributed under the Apache License. See `LICENSE.txt` for more information.
