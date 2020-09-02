# -*- coding: utf-8 -*-
from odoo import http 
import json 

#ceration de la classe couture 

#class salon_de_Conture(http.Controller):
#    @http.route("/couturier", type="http", auth="none", methods=['GET'])
#    def afficher(self):
#        print("Requete lancée")
#        text = '<h1>Voir tous les contacts </h1>'
#        return text



class salon_de_Conture(http.Controller):
    @http.route("/couturier", type="http", auth="none", methods=['GET'])
    def afficher(self):
        allcontacts = http.request.env['salon_de__couture.salon_de__couture'].sudo().search([]) 
        monhtml = ''
        mescontacts = []

        if len(allcontacts) <= 0 :
            msg ='Aucune donnée'
            mescontacts = []
        else:
            msg ='tous les contact'
            for salon_de__couture in allcontacts:
                
                dictContact = {
                    'id' : salon_de__couture.id,
                    'nom': salon_de__couture.nom.name,
                    'prenom': salon_de__couture.prenom,
                    'age': salon_de__couture.age,
                    'date_de_naissance': str(salon_de__couture.date_de_naissance),
                    'specialite': salon_de__couture.specialite,
                    'contact': salon_de__couture.contact
                }
                mescontacts.append(dictContact)

        data = {"success": True, "contacts": mescontacts, "msg": msg, 'nb':len(allcontacts)}
        return json.dumps(data)
    

    @http.route("/create/couturier", auth="none", type="json", methods=['POST'])
    def createContact(self, **kwargs):
        nom = kwargs['nom']
        prenom = kwargs['prenom']
        age = kwargs['age']
        date_de_naissance = kwargs['date_de_naissance']
        specialite = kwargs['specialite']
        contact = kwargs['contact']
        

        vals = {
            'nom' : nom,
            'prenom' : prenom,
            'age': age,
            'date_de_naissance': date_de_naissance,
            'specialite': specialite,
            'contact':contact
        }
        creation =  http.request.env['salon_de__couture.salon_de__couture'].sudo().create(vals)

        if creation:
            message = 'Succes ' 
            return message
        else:
            message = 'erreur lors de la creation ' 
            return message 





