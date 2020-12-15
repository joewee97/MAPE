# MAPE
M.A.P.E., short for Monitoring Automated Plant Ecosystem. This project is used to monitor environmental factors that can best nurture a plant's requirement.

Using a Raspberry Pi, it collects data variables using sensors and execute actions based on the data collected using MySQL and stored in a database and accessible through a web-based UI using PHP and HTML.

Sensors and modules are instructed to do the following using Python:
•DHT11, a sensor that to detect temperature and humidity.
•Soil moisture sensor, used to detect moisture in a soil.
•Light Dependent Resistor (LDR), to measure amount of light intensity through resistance changes.

•Water float sensor, to indicate a lack of water in a container. Low water storage will trigger an SMTP to email the user.


•Water pump with relay module, toggles on when soil moisture sensor detects absence of moisture.

•Lamp with relay module, toggles on whenever condition is met (low light intensity).

