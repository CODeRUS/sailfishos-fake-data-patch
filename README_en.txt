all actions need to be done in the terminal.

for convenience, the file can be renamed to fake_data.patch and put in a home folder.

in the terminal:

devel-su

to apply the patch:

patch -p 1 -d / -i /home/nemo/fake_data.patch

to roll back the patch:

patch -R -p 1 -d / -i /home/nemo/fake_data.patch

if it says that the patch is not installed, you need to perform:

pkcon install patch

Next, you need to exit the devel-su command

exit

use the following commands to modify the data:

the operator name on the SIM card 1:

dconf write / desktop / lipstick-jolla-home / ril_0_fakeName '"Operator 1"'

the name of the operator on the SIM card 2:

dconf write / desktop / lipstick-jolla-home / ril_1_fakeName '"Operator 1"'

Mobile Internet connection name:

dconf write / desktop / lipstick-jolla-home / fake_connectionName '"Internet"'

operator name on the lock screen:

dconf write / desktop / lipstick-jolla-home / fake_operatorName '"Operator"'

IMEI numbers:

dconf write / desktop / lipstick-jolla-home / fakeImei '"123456789012345, 123456789012346"'

bluetooth address:

dconf write / desktop / lipstick-jolla-home / fakeBluetooth '"10: 20: 30: 40: 50: 60"'

address wlan:

dconf write / desktop / lipstick-jolla-home / fakeWlan '"10: 20: 30: 40: 50: 60"'
