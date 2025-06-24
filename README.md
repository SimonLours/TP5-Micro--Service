# TP5-MicroService (Axel Pedrero / Simon Lours)

# Blagues.pdf

## Questions de compréhension

### Pourquoi faire des petits services ?

1. Pourquoi voudrait-on diviser un gros service web en plusieurs morceaux plus petits ?
   
   Pour gagner en modularité car chaque petit service est plus facil à comprendre, maintenir, tester et déployer. Cela permet d’isoler les changement sans impacter tout le système
   
2. Imaginez que vous travaillez sur un gros projet. Que se passe-t-il si vous devez modifier une seule fonctionnalité ? Est-ce facile ? Risqué ?
   
   Dans un gros projet, modifier une seule fonctionnalité peut être complexes et risqué, car cela peut avoir des impacts involontaires ailleurs
   
3. Peut-on confier un petit service à une autre équipe ou un autre développeur sans qu'il ait besoin de connaître tout le reste ?

   Oui, c’est un avantage clé des microservices car chaque service est autonome et on peut l’attribuer a une autre équipe ou a un développeur sans qu’ils ait à connaître tout le système
   
4. Que se passe-t-il si une partie tombe en panne ? Peut-on réparer sans tout redémarrer ?

   Oui, dans une architecture microservices, chaque service fonctionne de manière indépendante. Si un service tombe en panne, on peut le redémarrer ou le remplacer sans affecter les autres.
   
5. Avez-vous déjà vu ou utilisé un site ou une appli qui semblait "modulaire" ?

    Par exemple : Amazon ouNetflix où chaque fonctionnalité (paiement, catalogue, suggestions,...) semble être un module à part


   
### Comment découper un service ?

6. Sur quels critères peut-on séparer un gros service en plusieurs petits ?

   Par fonctionnalité (par exemple : blagues, météo, ...), par type de données manipulées, ou par responsabilités métiers distinctes
   
7. Faut-il découper par fonctionnalité (ex : blague, météo, ...) ? Par type de donnée ? Par public cible ?

   Il est généralement préférable de découper par fonctionnalité. Chaque microservice doit gérer une seule responsabilité claire. Mais les autres critères peuvent aussi être pertinents selon le contexte.
   
8. À partir de combien de lignes de code ou de routes HTTP faut-il envisager un découpage ?

     Il n’y a pas de règle fixe, mais si le code devient difficile à maintenir, tester ou comprendre, ou si le service a trop de routes HTTP, c’est un bon indicateur pour envisager un découpage.
    
9. Le découpage doit-il être figé ou peut-il évoluer ?

    Il doit pouvoir évoluer. L’architecture logicielle est vivante : les besoins changent, et l’organisation du code doit pouvoir s'adapter sans tout réécreire



------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Météo.pdf
