U
    ���^�  �                   @   s�  d dl Z d dlZd dlZd dlZe�d� e�d� e�d� e�d� e �d� e�d� dZdd� Zee� d	� ze	d
d�Z
e
�� Ze
j W nJ   eed��Ze	d
d�Z
e
�e� e
j e	d
d�Z
e
�� Ze
j Y nX z&e	dd�Z
e	dd�Z
e
�� Ze
j W nJ   eed��Ze	dd�Z
e
�e� e
j e	dd�Z
e
�� Ze
j Y nX zd dlZW nB ek
�r�   ed� e�d� ed� e�d� d dlZY nX dd� Zdd� Zedk�r�e�  dS )�    N�clearzHtoilet -f smblock --filter border:metal '=============================='zCtoilet -f smblock --filter border:metal '~ ~ AnNoY   CreaTionS ~ ~'�   zE[1;34;40m
#########################################################
c                   C   s6   t �d� td� td� td� td� td� d S )Nz:toilet -f smblock --filter border:metal '~ ~ Mega Run ~ ~'z,[1;35;40m--------------------------------,
z-[0;37;46m| Author    : Annoy Creations   |,
z-[0;37;46m| Telegrame : t.me/hackerrdt    |,
z-[0;37;46m| FaceBook  : Network Hacker    |,
)�os�system�print� r   r   �D:\projects\mega run\game.py�name   s    
r	   �
zauth.txt�rz[1;36;40mAuth :- �wzurl.txtz[1;36;40mURL :- z,%s Requests isn't installed, installing now.zpip3 install requestsz%s Requests has been installed.c                  C   s&  t �d� tt� d� dtdd�} t}d}t�d� d}tj	|| d�}t
|�}|d	krptt� td
� tt� n:|dkr�tt� td� tt� ntt� td� tt� |d7 }tdt
|�ddd� td�D ]@}|d d }tdt
t|��d dd� t�d� tj�d� q�q4t �d� t�  d S )Nr   r
   zmegarun.dialog.lkz
2018.3.0f2)ZHostZAuthorizationzX-Unity-Versionr   �Z   )Zheadersz<Response [204]>z)
[0;37;42m------Not Recieved Data------ z<Response [200]>z1
[0;37;42m ---- $ You have Recieved Data $ ---- z/
[0;37;41m ---- You may be a Blocked User ----�   z[1;34;40m
zPlz  Wait For Next round� )�end�   �d   z[0;34;47m
>>> [#]z% g      �?z[Fztoilet Mission Complete!!!)r   r   r   r	   �auth�url1�time�sleep�requests�get�str�bar�range�int�sys�stdout�write�again)�header�url�ss�size�resZresp�iZprr   r   r   �main@   s@    
 �




r'   c                  C   sJ   t d�} | dks| dkr t�  n&| dks0| dkr8t�  ntd� | �  d S )Nz)[1;36;40m
Do You want use again (y/n) - �y�Y�n�Nz[1;31;40mEnter valid letter)�inputr'   �quitr   )r    r   r   r   r    g   s    r    �__main__)r   �urllibr   r   r   r   r   r	   r   �open�f�readr   �closer   r,   �wrr   r   r   �ImportErrorr'   r    �__name__r   r   r   r   �<module>   sb   


















'
