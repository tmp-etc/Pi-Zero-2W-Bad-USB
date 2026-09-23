use systemd-analyse (blame / critical-chain) to see how you speed up the os loading

rfkilling wifi / bl helps

so does disabling swap

as do prolly these settings in config.txt

```
boot_delay=0
disable_splash=1
dtoverlay=disable-bt
camera_auto_detect=0
display_auto_detect=0
initial_turbo=30
```
