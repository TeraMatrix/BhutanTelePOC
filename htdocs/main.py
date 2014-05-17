#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
# +------------------------------------------------------------------+
# |             ____ _               _        __  __ _  __           |
# |            / ___| |__   ___  ___| | __   |  \/  | |/ /           |
# |           | |   | '_ \ / _ \/ __| |/ /   | |\/| | ' /            |
# |           | |___| | | |  __/ (__|   <    | |  | | . \            |
# |            \____|_| |_|\___|\___|_|\_\___|_|  |_|_|\_\           |
# |                                                                  |
# | Copyright Mathias Kettner 2013             mk@mathias-kettner.de |
# +------------------------------------------------------------------+
#
# This file is part of Check_MK.
# The official homepage is at http://mathias-kettner.de/check_mk.
#
# check_mk is free software;  you can redistribute it and/or modify it
# under the  terms of the  GNU General Public License  as published by
# the Free Software Foundation in version 2.  check_mk is  distributed
# in the hope that it will be useful, but WITHOUT ANY WARRANTY;  with-
# out even the implied warranty of  MERCHANTABILITY  or  FITNESS FOR A
# PARTICULAR PURPOSE. See the  GNU General Public License for more de-
# ails.  You should have  received  a copy of the  GNU  General Public
# License along with GNU Make; see the file  COPYING.  If  not,  write
# to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
# Boston, MA 02110-1301 USA.

import defaults, config

def page_index():
    start_url = html.var("start_url", config.start_url)
    html.req.headers_out.add("Cache-Control", "max-age=7200, public");
    if "%s" in config.page_heading:
        heading = config.page_heading % (defaults.omd_site or _("Multisite"))
    else:
        heading = config.page_heading

    html.write("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta http-equiv="content-type" content="text/html; charset=UTF-8">
    <meta charset="utf-8">
     <title>Bhutan Telecom | %s</title>
    <link rel="shortcut icon" href="images/favicon.ico" type="image/ico">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1, user-scalable=no">
    <meta name="description" content="">
    <meta name="author" content="">
    <link rel="stylesheet" type="text/css" href="theme/css/cloud-admin.css" >
    <link rel="stylesheet" type="text/css"  href="theme/css/themes/default.css" id="skin-switcher" >
    <link rel="stylesheet" type="text/css"  href="theme/css/responsive.css" >
    <!-- STYLESHEETS --><!--[if lt IE 9]><script src="js/flot/excanvas.min.js"></script><script src="http://html5shiv.googlecode.com/svn/trunk/html5.js"></script><script src="http://css3-mediaqueries-js.googlecode.com/svn/trunk/css3-mediaqueries.js"></script><![endif]-->
    <link href="theme/font-awesome/css/font-awesome.min.css" rel="stylesheet">
    <!-- ANIMATE -->
    <link rel="stylesheet" type="text/css" href="theme/css/animatecss/animate.min.css" />
    <!-- DATE RANGE PICKER -->
    <link rel="stylesheet" type="text/css" href="theme/js/bootstrap-daterangepicker/daterangepicker-bs3.css" />
    <!-- TODO -->
    <link rel="stylesheet" type="text/css" href="theme/js/jquery-todo/css/styles.css" />
    <!-- FULL CALENDAR -->
    <link rel="stylesheet" type="text/css" href="theme/js/fullcalendar/fullcalendar.min.css" />
    <!-- GRITTER -->
    <link rel="stylesheet" type="text/css" href="theme/js/gritter/css/jquery.gritter.css" />
    <!-- FONTS -->
    <link href='http://fonts.googleapis.com/css?family=Open+Sans:300,400,600,700' rel='stylesheet' type='text/css'>
</head>
<frameset cols="280,*" frameborder="0" framespacing="0" border="0">
    <frame src="side.py" name="side" noresize scrolling="no">
    <frame src="%s" name="main" id="main_frame" noresize>
</frameset>
</html>
""" % (heading, start_url))

# This function does nothing. The sites have already
# been reconfigured according to the variable _site_switch,
# because that variable is processed by connect_to_livestatus()
def ajax_switch_site():
    pass
