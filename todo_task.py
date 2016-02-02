# -*- coding: utf-8 -*-
from openerp import models, fields, api
class TodoTask(models.Model):
    _name = "todo.task"
    _inherit = ['todo.task', 'mail.thread']
    user_id = fields.Many2one('res.users', 'Responsible')
    date_deadline = fields.Date('Deadline')

    name = fields.Char(help="What needs to be done?")

    @api.one
    def do_toggle_done(self):
        if self.user_id != self.env.user:
            raise Exception('Only the responsible can do this!')
        else:
            return super(TodoTask, self).do_toggle_done()
