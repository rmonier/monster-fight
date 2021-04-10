# MONSTER FIGHT

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/rmonier/monster-fight">
    <img src="DEPENDANCES/images/icone.ICO" alt="Logo" width="130">
  </a>

<h3 align="center"><a href="https://github.com/rmonier/monster-fight"><img src="DEPENDANCES/images/menus/titre.gif" alt="monster-fight" width="380"></a></h3>

  <p align="center">
    Jeu ISN
    <br />
    <a href="https://github.com/rmonier/monster-fight/wiki"><strong>Lire le wiki »</strong></a>
    <br />
    <br />
    <a href="https://github.com/rmonier/monster-fight/releases">Voir les Releases</a>
    ·
    <a href="https://github.com/rmonier/monster-fight/issues">Issues</a>
    ·
    <a href="https://github.com/rmonier/monster-fight/projects">Voir le Projet</a>
  </p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table des Matières</summary>
  <ol>
    <li>
      <a href="#à-propos-du-projet">À Propos du Projet</a>
      <ul>
        <li><a href="#créé-avec">Créé avec</a></li>
      </ul>
    </li>
    <li>
      <a href="#commencer">Commencer</a>
      <ul>
        <li><a href="#prérequis">Prérequis</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#utilisation">Utilisation</a></li>
    <li><a href="#arborescence">Arborescence</a></li>
    <li><a href="#crédits">Crédits</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

***

<!-- ABOUT THE PROJECT -->
## À Propos du Projet
Jeu réalisé en 2015/2016 avec Joris Coulange pour le projet final d'ISN en classe de Terminale. Ajout en 2021 sur GitHub avec un README et une utilisation du gestionnaire de packages pipenv.

### Créé avec
* [Python](https://www.python.org/)
* [Pygame](https://www.pygame.org/)

<!-- GETTING STARTED -->
## Commencer

### Prérequis

* Installer la dernière version de pyenv (https://github.com/pyenv/pyenv-installer [ UNIX ], https://pyenv-win.github.io/pyenv-win/ [ WINDOWS ]) ou le mettre à jour avec la commande suivante :
  ```sh
  pyenv update
  ```
* Installer la dernière version de pipenv (https://pipenv.pypa.io/) ou le mettre à jour avec la commande suivante :
  ```sh
  pip install pipenv --upgrade
  ```

### Installation

1. Cloner le dépôt sur votre machine
   ```sh
   git clone https://github.com/rmonier/monster-fight.git
   ```
2. À la racine de MONSTER FIGHT, installer les dépendances
   ```sh
   pipenv install --dev
   ```
> :warning: **Si vous utilisez pyenv-win (WINDOWS)** : Si vous n'avez pas la version de Python utilisée dans le projet, il est possible que pipenv ne détecte pas pyenv, vous empêchant de l'utiliser directement. Pour régler ce problème, installez d'abord la version voulue `pyenv install x.x.x` puis au lieu de la commande ci-dessus utilisez celle-ci : `pipenv --python %USERPROFILE%\.pyenv\pyenv-win\versions\x.x.x\python.exe install --dev`
3. MONSTER FIGHT est maintenant installé.

<!-- USAGE EXAMPLES -->
## Utilisation

Utiliser la commande suivante pour lancer MONSTER FIGHT :
  ```sh
  pipenv run run
  ```

Pour générer un exécutable compatible avec la machine utilisée, lancer la commande suivante :
  ```sh
  pipenv run build
  ```

***

<!-- TREE STRUCTURE -->
## Arborescence
<details>

_TODO_

</details>

<!-- CREDITS -->
## Crédits

Romain Monier [ [GitHub](https://github.com/rmonier) ] – Co-développeur 
<br>
Joris Coulange – Co-développeur

<!-- CONTACT -->
## Contact

Lien du Projet : [https://github.com/rmonier/monster-fight](https://github.com/rmonier/monster-fight)