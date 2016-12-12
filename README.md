Purpose
-------

To provide a systemd service file and nicer packaging for the HDHomeRun DVR service.

Building
--------

Run "dpkg-buildpackage -b" in this repository.

Usage
-----

The package will ask for the recordings directory at install time.  The config file
is written out to /var/lib/hdhr/hdhomerun_record.conf (which is also referenced by
the systemd service file).  To reconfigure it later, use

    "dpkg-reconfigure hdhomerun-dvr
