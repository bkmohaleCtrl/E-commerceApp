# E-commerceApp


step 1: Project Setup_

     Cmd : ....cd Desktop
            ....mkdir E-commerceApp
            ...cd E-commerceApp then \E-commerceApp>code .                  ----> opening in VScode

    install virtualenv : (run)---> pip install virtualenv

                        virtualenv (name)--> 'ecommerceenv' 
        activate env : \E-commerceApp> ecommerceenv\Scripts\activate   

        after activating (run) : pip install django  

                     next(run) :  django-admin startproject ecommerceApp

                     next(run) :  cd ecommerceApp

                        (run)  : python manage.py startapp mystore   ............"mystore" as the name 
