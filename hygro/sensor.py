
import subprocess
import logging

LOG = logging.getLogger(__name__)

python = '/srv/robotice/bin/python2'
executable = "/srv/robotice/sensors/hygro/driver.py"

plain = False

try:
  sys.path.append("/srv/robotice/service")
  from robotice.utils import call_command
except Exception, e:
  plain = True
  LOG.debug("Robotice lib not found")

def get_data(sensor):

    port = str(sensor.get('port'))

    arch = sensor.get('cpu_arch')

    reverse = sensor.get("reverse", False)

    command = [
        python,
        driver_path,
        '-a', str(arch),
        '-p', str(port),
        '-t' % sensor.get("type").lower()]

    if plain is True:
        output = subprocess.check_output(command)
    else:
        output = call_command(command)

    data = []

    metric_format = "{0}.hygro_{1}"

    data.append(
        (metric_format.format(sensor.get('name'), sensor.get("type").lower()), output,))

    return data
