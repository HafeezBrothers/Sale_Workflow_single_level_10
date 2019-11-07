{

    'name':'Sale Order WorkFlows',
    'description' : 'SO WorkFlows',
    'license': 'LGPL-3',
    'version' : '1.0',
    'author' : 'Hafeez Brothers',
    
    'depends' : [
                   'base', 'product','sale',
                ],
    'data' :[   
                
                'views/sale_cust.xml',
                'security/hr_user_rights.xml'
            ],
    'installable' : True,
    'price':25.00,
    'currency':'EUR', 
    

}
