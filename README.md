# pimify
![GitHub License](https://img.shields.io/github/license/suriya-mca/pimify) ![GitHub commit activity](https://img.shields.io/github/commit-activity/t/suriya-mca/pimify) ![GitHub Repo stars](https://img.shields.io/github/stars/suriya-mca/pimify?style=flat&color=pink) ![GitHub forks](https://img.shields.io/github/forks/suriya-mca/pimify?style=flat&color=yellow) ![GitHub Release](https://img.shields.io/github/v/release/suriya-mca/pimify?color=green)

Pimify is an open-source Product Information Management (PIM) platform

![image](https://github.com/user-attachments/assets/58157365-d1ea-4aa7-8556-a717c73861c4)

## 	⚡ Quick Installation with Script

You can set up the project quickly by running the installation script. Make sure you have the necessary permissions.

### Prerequisites

Ensure the following is installed on your system:

- **Python** (version 3.7 or higher)

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
  DEBUG = False
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

## 🐋 Docker Installation

If you prefer to use Docker for a containerized setup, follow these steps:

### Prerequisites

Ensure the following is installed on your system:

- **Docker**

### Clone the project

```bash
  git clone https://github.com/suriya-mca/pimify.git
```

### Go to the project directory

```bash
  cd pimify
```

### Build and run the docker image

```bash
  docker build -t pimify:latest .
  docker run -p 8000:8000 --name pimify-container pimify:latest
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
