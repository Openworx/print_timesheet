# -*- coding: utf-8 -*-
{
    'name' : 'Print Timesheet Activities',
    'version' : '1.0',
    'category': 'Human Resources',
    'summary' : 'Print Timesheet Activities',
    'description': """
    This module is a backport from Odoo 10.0 https://github.com/odoo/odoo/blob/10.0/addons/hr_timesheet/report/report_timesheet_templates.xml.
    """,
    'author' : 'Openworx',
    'website' : 'http://www.openworx.nl',
    'depends' : ['account', 'hr', 'base', 'hr_attendance'],
    'data' : ['report/report_timesheet.xml',],
    'installable' : True,
    'application' : False,
}
