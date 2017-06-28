все действия нужно делать в терминале.

для удобства файл можно переименовать в ```fake_data.patch``` и положить в домашнюю папку.

в терминале:

```
devel-su
```

для применения патча:

```
patch -p 1 -d / -i /home/nemo/fake_data.patch
```

для отката патча:

```
patch -R -p 1 -d / -i /home/nemo/fake_data.patch
```

если говорит, что не установлен ```patch``` нужно выполнить:

```
pkcon install patch
```

далее нужно выйти из ```devel-su``` командой

```
exit
```

для изменения данных использовать следующие команды:

имя оператора на СИМ карте 1:

```
dconf write /desktop/lipstick-jolla-home/ril_0_fakeName '"Operator 1"'
```

имя оператора на СИМ карте 2:

```
dconf write /desktop/lipstick-jolla-home/ril_1_fakeName '"Operator 1"'
```

Название подключения мобильного интернета:

```
dconf write /desktop/lipstick-jolla-home/fake_connectionName '"Internet"'
```

название оператора на экране блокировки:

```
dconf write /desktop/lipstick-jolla-home/fake_operatorName '"Operator"'
```

IMEI номера:

```
dconf write /desktop/lipstick-jolla-home/fakeImei '"123456789012345, 123456789012346"'
```

адрес bluetooth:

```
dconf write /desktop/lipstick-jolla-home/fakeBluetooth '"10:20:30:40:50:60"'
```

адрес wlan:

```
dconf write /desktop/lipstick-jolla-home/fakeWlan '"10:20:30:40:50:60"'
```