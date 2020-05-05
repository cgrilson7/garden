## GardenHelper
Automated, intelligent gardening support system serving as groundhog deterrent, irrigation system, bird classifier, and much more.

## Requirements

Python 3.7

`venv` for package management, storage of secrets in `[venv_name]/bin/activate` script.

Pseudo-distributed `apache-airflow` environment configured with `postgres` (and `pscyopg2+postgresql` driver) for DAG management.
- `$AIRFLOW_HOME` set to `garden/airflow` directory, containing `dags` folder. See `airflow/airflow.cfg` for example configuration. 
- For setup, see [this guide](https://stlong0521.github.io/20161023%20-%20Airflow.html) by Tianlong Song.

`mongodb` for persistent storage.

[OpenWeather API key](https://openweathermap.org/api) stored in `[venv_name]/bin/activate`.