# Graylog WALKOFF App
The Graylog WALKOFF App aims to provide WALKOFF orchestration for conducting searches against the Graylog API. 

[Graylog](https://www.graylog.org/) is a wonderful open source log management platform that is robust, speedy and reliable.

[WALKOFF](https://github.com/iadgov/WALKOFF) is an OSS project made by the NSA that provides an automation framework for automating repetitive tasks.

## Installation
1. Clone the repo
```
git clone https://github.com/billmurrin/graylog-walkoff-app.git
```
2. Copy the Graylog directory to WALKOFF/apps directory
3. From the WALKOFF directory, install the package dependencies in requirements.txt
```
# python installDependencies -a Graylog
```
4. Start, or restart, the WALKOFF web server
```
# python startServer.py
```
5. In the WALKOFF Web interface, configure the Graylog device
- The *App* is "Graylog"
- The *Type* is "Graylog"
- The URI to Graylog (E.g. http://ip-to-graylog:9000). No need to include /api.
- The API key to use for the connection.

## Usage
You can use the sample workflow under the samples directory as an example to see how the Graylog App works. 

Just copy the Graylog.playbook file to your data/workflows folder and restart the WALKOFF server.

## Current App Actions (More to follow)
1. **param**

The param action allows you to set a parameter for the search. 
E.g. limit, range, fields, filter

2. **relative_search**

Specify the query to run, required params (E.g. fields, range) should be set using the param action.

## Way Ahead
1. Support additional query actions (absolute search, relative terms, etc.).
2. Provide sample workflows.
3. Update app.py once WALKOFF issue #165 has been resolved.
4. Implement tests using pytest.
5. Widget for the App? Maybe...