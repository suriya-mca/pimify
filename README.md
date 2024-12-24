# pimify
![GitHub License](https://img.shields.io/github/license/suriya-mca/pimify) ![GitHub commit activity](https://img.shields.io/github/commit-activity/t/suriya-mca/pimify) ![GitHub Repo stars](https://img.shields.io/github/stars/suriya-mca/pimify?style=flat&color=pink) ![GitHub forks](https://img.shields.io/github/forks/suriya-mca/pimify?style=flat&color=yellow) ![GitHub Release](https://img.shields.io/github/v/release/suriya-mca/pimify?color=green)

Pimify is an open-source Product Information Management (PIM) platform

![image](https://github.com/user-attachments/assets/58157365-d1ea-4aa7-8556-a717c73861c4)

## 	⚡Quick Installation with Script

You can set up the project quickly by running the installation script. Make sure you have the necessary permissions.

### Prerequisites

Ensure the following is installed on your system:

- **Python** (version 3.10 or higher)

### Clone the project & Go to the project directory

```bash
git clone https://github.com/suriya-mca/pimify.git
cd pimify
```

### Create .env file

```bash
SECRET_KEY=secret_key
DEBUG=False
DOMAIN=http://your-domain.com
OPEN_EXCHANGE_RATES_APP_ID=None
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

### Clone the project & Go to the project directory

```bash
git clone https://github.com/suriya-mca/pimify.git
cd pimify
```

### Create .env file

```bash
SECRET_KEY=secret_key
DEBUG=False
DOMAIN=http://your-domain.com
OPEN_EXCHANGE_RATES_APP_ID=None
```

### Build and run the docker image

```bash
docker build -t pimify:latest .
docker run --env-file .env -p 8000:8000 --name pimify-container pimify:latest
```

### Create superuser
```bash
docker exec -it container-id sh
/app > python manage.py createsuperuser # create superuser
```

## 📂 Important Folders

Pimify relies on three main folders for data storage and management. Make sure these folders are properly configured in your environment:

1. **`data/`**: 
   - Stores the actual database file.

2. **`backups/`**: 
   - Contains database backups (last 3 months by default).
   - You can update this setting in the `scheduler.py` file if you want to adjust the backup retention period.

3. **`media/`**: 
   - Stores image and video files.

Ensure these folders are persisted properly when running Pimify in a containerized or production environment.

## 🚀 Getting Started

Once the server starts, you can access the following URLs:

- **Dashboard**: [http://127.0.0.1:8000/dashboard/](http://127.0.0.1:8000/dashboard/)
- **API Documentation**: [http://127.0.0.1:8000/api/v1/docs](http://127.0.0.1:8000/api/v1/docs)

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
