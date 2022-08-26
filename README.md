# DataCollection
## Description des méthodes implémentées:
*class* html.**HtmlFactory**, csv.**CsvFactory**, json.**JsonFactory**
 **addCurrency**(cls,data):
Ajoute une nouvelle colonne "currency" dans *data* puis la retourne.
Et avant d'être retourné chaque ligne de *data* se verra attribuée un currency choisi aléatoirement sur une liste contenant des devises.
 **addAddress**(cls, data):
*(seulement dans html.**HtmlFactory**)*
De même que la méthode ***addCurrency*** mais cette fois une colonne adresse est ajoutée et la liste contient des adresses.
 **addSalaryXOF**(cls, data):
Pour chaque élémment de ***data***, elle récupère 
Ajoute une nouvelle colonne "salary_xof" sur chaque élément de ***data*** ,
 **addCountryAndFlag**(cls, data):
Récupère et affecte dans une variable *countries* le résultat de la fonction *country.CountryFactory.main()*
Définit une fonction *country(row)* dans laquelle les variables *START*,*FINAL*,*index* et *country* sont créées.
*START*: est la borne minimale
*FINAL*: est la borne maximale et est égale *len(countries)-1*
*index*: contient le resultat retourné par la fonction *utils.Utils.randomize()*
*country*: est l'élément se trouvant dans *countries[index]*
Puis modifie respectivement les valeurs des clefs *country* et *flag* de *row* par *country.get('name')* et *country.get('flag')*
Et enfin retourne row.
Crée une variable *data* et lui stocke le résultat de la fonction *map()* et lui donne en paramètre la fonction *country* et ***data***
Puis convertit en list et retourne *data*

*class* utils.**Utils**
 **concatenate**(cls,*args):
  Crée une liste vide, puis parcours la liste des arguments si l'argument   est une liste elle le concatène avec la liste créée sinon elle fait rien,   et enfin retourne la liste.
 **convertToXOF**(cls,amount,devise,currencies):
  Convertit ***currencies*** en pandas.DataFrame.
  Recherche  ***devise*** dans ***currencies*** et affecte le résultat dans *currency*, aprés récupère  la clé achat dans *currency* et l'affecte à la variable *achat*. Enfin retourne le produit de ***amount*** et *achat*.

*class* currency.**Currency**
  **fetcher**(cls,url):
   Fait appel à *requests.get()* et lui passe ***url*** en paramètre puis retourne le résultat sous format texte.
 **getRows**(cls,html):
  Crée un objet *data* de la classe *bs4.BeautifulSoup()* et lui passé  en paramètre ***html*** et *features*="html.parser".
Puis récupère tous les 'tr' contenus dans *data* et l'affecte dans *rows*, et enfin retourne tous les éléments de *rows* sauf le premier qui correspond à l'entête de la table.
  **getCurrencies**(cls,rows):
Crée une liste vide *currencies*, puis parcours pour tous les éléments de ***rows***, récupère les 'td', crée une variable *currency* de type dict et l'ajoute dans *currencies*, et enfin retourne *currencies*.
*class* database.**Db**
  **getConnection()**:
Fait appel à la fonction *sql.**connect()*** et lui passe le chemin de la base de données en paramètre et affecte l'objet tetourné dans la variable *connection*, et enfin retourne la variable *connection*.

*class* database.**Database**
  **insertDataToDatabase(self,data)**:
Récupère les clefs du premier élément de ***data*** et le stocke dans la variable *keys*, aprés crée une liste *values* où elle stocke sous forme de tuple les valeurs contenues dans chaque élément de ***data***.
Crée une instance de connection, puis de la connection crée une varaible *cursor* grâce à la fonction *cursor()*.
Et enfin fait appel à la fonction *executemany()* de *cursor* en lui passant en paramètre *requete=requete = f"INSERT INTO person {keys} values(?,?,?,?,?,?,?,?,?,?,?)"* et *values* et fait un commit.
  **getValues(cls)**
Crée un objet *connection* qui est une instance de *Db .getConnection()*, de *connection* elle crée la variable *cursor*. Avec *cursor*, elle éxeécute la fonction *execute()* en lui passant en paramètre *requete="Select * from person*.
Parcourt *cursor.description* et recupère le premier élément et le stocke dans la liste *keys*.
Crée une variable *values* et l'affecte le resultat de *cursor.fetchall()*
Puis fait appel à la fonction *cls.toListOfDicts()* et lui passe en paramètre *keys*,*values* et enfin retourne le résultat retourné par cette fonction.
  **toListOfDicts(cls,keys,values)**
Crée une liste vide *liste*, récupère la longueur de ***keys*** et l'affecte dans la variable *length* .
Parcourt ***values*** et crée une variable *elt* de type dict où chaque les paires clef/valeur sont obtenues grâce à un parcours sur *range(length)* et que chaque paire correspond *keys[i]:value[i]*.
*NB:i correspond à l'élément de parcours sur range(length) et value sur **values***
Puis ajoute *elt* dans *liste*, et enfin retourne *liste*.
    
## Comment Démarrer le projet?
- Clônez d'abord le repository
- Ouvrez le dossier dans votre éditeur de texte ou IDE
- Ouvrez un terminal et placez vous dans le chemin du dossier
- Créer et activer un environnement virtuel:
- Installer tous les librairies utilisées en tapant:
    ```
    pip install -r requirements.txt
    ```
- Démarrer le projet en tapant:
    ```
    uvicorn main:app --reload  
    ```

Si tous ces étapes sont bien éxecutées, vous n'avez qu'à ouvrir votre navigateur tapez cet url : http://127.0.0.1:8000/persons et le tour est joué.

