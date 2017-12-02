# Raspberry client for labadmin


### Instructions


• Install jessie lite<br />

• Use raspi-config to enable ssh<br />

• Use raspi-config to enable auto login without password<br />

```
sudo reboot

sudo apt-get update

sudo apt-get install python-pigpio python-smbus

sudo apt-get install python-smbus

sudo mv autostart.sh /etc/init.d/

chmod +x /etc/init.d/autostart.sh

sudo update-rc.d autostart.sh defaults

sudo reboot
```


### Pinout
```
RED_PIN=17    // Red Led
GREEN_PIN=27  // Green Led
RELAY1_PIN=2  // External door
RELAY2_PIN=3  // Fablab door
```

### Wiring

![](Raspberry/OfficineDoor.png)
