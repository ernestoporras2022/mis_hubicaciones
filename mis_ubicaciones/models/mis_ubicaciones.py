from odoo import models, fields, api

class MisUbicaciones(models.Model):
    _name ="mis.ubicaciones"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    tienda = fields.Char(string = "Tienda", required=True, tracking="1")
    direccion =fields.Text(string= "Direccion")
    registro_federal =fields.Char(string="Registro federal")
    inicial_en_caja =fields.Float(string="Inicial en caja")
    ancho_ticket_ids = fields.Many2one(comodel_name="ancho.ticket", string="Ancho de imprecion de ticket")

    anchoReporte = [
        ('carta', 'Carta'),
        ('oficio', 'Oficio'),
        ('dbcarta', 'Doble carta'),
    ]
    ancho_reporte = fields.Selection(anchoReporte, default=anchoReporte[0][0])

    comision_credito = fields.Float(string="% Comision pagos con targeta de credito")
    comision_debito = fields.Float(string="% Comision pagos con targeta de debito")


    telefono = fields.Char(string="Telefono ")
    web_email = fields.Char(string="Web / Email")
    horario = fields.Char(string="Horario")
    encargado_ids= fields.Many2one(comodel_name="nombre.encargado", string="Encargado")
    rfc = fields.Char(string="R.F.C.")
    iva = fields.Float(string="% IVA")



class AnchoTicket(models.Model):
    _name = "ancho.ticket"
    _rec_name = "nombre"

    nombre = fields.Char(string="Nombre")


class Encargado(models.Model):
    _name = "nombre.encargado"
    _rec_name = "name"

    name = fields.Char(string="Nombre del encargado")



