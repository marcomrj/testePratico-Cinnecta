
def validator(password,requirements):

    try:
        assert (len(requirements) == 3), "Lista de requerimentos com tamanho errado."

        assert (requirements[0] in ('LEN','LETTERS','NUMBERS','SPECIALS')),"Erro no primeiro requisito."
    
        assert (requirements[1] in ('<','>','==')),"Erro no segundo requisito."
    
        assert (type(requirements[2]) == int ),"Erro no terceiro requisito."

        assert(len(password) != 0), "A senha não possui nenhum caractere."
    except Exception as ex:
        print(ex)
        return False

    if requirements[0] == 'LEN':
        if requirements[1] == '<':
            if len(password) < requirements[2]:
                return True
        elif requirements[1]== '>':
            if len(password) > requirements[2]:
                return True
        elif requirements[1]== '==':
            if len(password) == requirements[2]:
                return True


    elif requirements[0] == 'LETTERS':
        if requirements[1] == '<':
            letters = sum(c.isalpha() for c in password)
            if letters < requirements[2]:
                return True
        elif requirements[1]== '>':
            letters = sum(c.isalpha() for c in password)
            if letters > requirements[2]:
                return True
        elif requirements[1]== '==':
            letters = sum(c.isalpha() for c in password)
            if letters == requirements[2]:
                return True


    elif requirements[0] == 'NUMBERS':
        if requirements[1] == '<':
            numbers = sum(c.isdigit() for c in password)
            if numbers < requirements[2]:
                return True
        elif requirements[1]== '>':
            numbers = sum(c.isdigit() for c in password)
            if numbers > requirements[2]:
                return True
        elif requirements[1]== '==':
            numbers = sum(c.isdigit() for c in password)
            if numbers == requirements[2]:
                return True


    elif requirements[0] == 'SPECIALS':
        password = password.replace(" ","")
        if requirements[1] == '<':
            specials =len(password)-sum([c.isdigit()+c.isalpha() for c in password])
            if specials < requirements[2]:
                return True
        elif requirements[1]== '>':
            specials =len(password)-sum([c.isdigit()+c.isalpha() for c in password])
            if specials > requirements[2]:
                return True
        elif requirements[1]== '==':
            specials =len(password)-sum([c.isdigit()+c.isalpha() for c in password])
            if specials == requirements[2]:
                return True
    
    return False


senha = '^Vw9LQ& p6ic!gDW15p39W7y Je7q8iXx5M9x^ @&^M7D yV7ZA0DG'
listateste = ['NUMBERS','>',5]
print(validator(senha,listateste))