## GardenHelper
Automated, intelligent gardening support system serving as groundhog deterrent, irrigation system, bird classifier, and much more.

## Requirements

- Python 3.7

- `venv` for package management

- Pseudo-distributed **Airflow** environment configured with **PostgreSQL** (and `pscyopg2+postgresql` driver) for DAG management.
  - `$AIRFLOW_HOME` set to `garden/airflow` directory, containing `dags` folder. See `airflow/airflow.cfg` for example configuration. 
  - For setup, see [this guide](https://stlong0521.github.io/20161023%20-%20Airflow.html) by Tianlong Song.

- **MongoDB** for persistent storage.

- [OpenWeather API key](https://openweathermap.org/api) stored in `[venv_name]/bin/activate`.

## Setup

- Edit the `mongod.conf` file in the root project directory, changing the paths to the `data/db` directory and to the `mongod.log` file. If you don't care about running `mongod` in daemon/detached mode, you can remove lines 1-7.

- Add the following lines to your `[venv_name]/bin/activate` script:

```bash
# Load secrets
export OPENWEATHER_API_KEY=[your API key]
export AIRFLOW_HOME=/path/to/garden/airflow/

# Start mongod in daemon mode, using mongod.conf file in root directory of this project
mongod --config mongod.conf

# Start airflow webserver at port 8080
airflow webserver -p 8080 -D

## Start airflow scheduler
airflow scheduler
```