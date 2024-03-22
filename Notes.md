2024.03.08. - konzi

- beolvasast nem kell az alairas objektumba tenni
- lehet kulon beolvasas
- beolvassa az osszes alairast
- dictionaryben tarolni id kat? signer objektum
- dictionary value erteke egy masik dic
- alairasok signature osztalyban eltarolni valtozoba
- data normalization - feature extraction? -(szarmaztatott tulajdonsagok kiszamitasa - kiszamitott ertekeket hozzaadni az alairasokhoz)


2024.03.13. - konzi

- normalization kijavitasa
- valtozokban eltarolni samplert aminek az egesz adatbazist oda adom
- kivalsztja mi az a training mi a masik 
- 2 mappabol - egyenloszamu eredeti es hamis a trainingbol es evaluation 
- nagyjabol a pdf et kovetve a ket adatb bol kivenni alairasokat, 
- 3 dataset kell - training amin tanul, validation- megtanulja aztan ellenorzi hogy mit csinalt, test dataset- amivel meg nem talalkozott
- epochon belul (iteracio a model tanitasanak)
- 2009es teszteleshez
- minden alaironak az alairasaibol veszek trainingbol 5-5 vagy 10-10 alairast - a ket dataset egyben adja ki a tarining es validation (70% a training 30 % validation)
- tesztelésre a sigcomp evaluation 5-10, svc tol minden amit nem hasznaltunk


2024.03.24 - self notes

- Scikit - learn: machine learning in python, data analysis (to split into train and test sets)
- os - operating system dependent funcionality 
- numpy - computation power (using arrays and matrixes with high level mathematics library)
- Keras - used for Neural networks 
- Seaborn - data visualization library based on matplotlib 
- Matplotlib - comprehensive library for creating static, animated, and interactive viasualizations

- os.path.basename() extracts the filename from a path string
- labeling data: assigning labels to subsets of data based on characteristics
- sklearn.preprocessing - normalizing
- sklearn.modelselection - splitting dataframe

- sigcomp 2009 NFI - forgery folder - 33 peoples signatures were forged by 6 writers 4 times (in the article 4 writes 6 times (24 forged sig / person)) - naming convention - NFI-<aaa>-forgerid <bb>-forgeduserid

- sigcomp 2009 NFI - genuine - 100 people 12 times (22 missing in reality, 88 writers combined genuine) - naming convention - NFI-<aaa> userid <bb> sigid 

- sigcomp 2009 Training - 1 - 12 genuine (12 * 5), 21 - 51 forged (32 * 12 * 5 ) - naming convention - NISDCC- <aaa> user id 

- epoch - one entire passing of training data through the algorithm

#### Kérdések következő konzira 
- A sigcomp 3 file training-forged-genuine egybe kell rakni az svc testing-training-evaluation -be?
- Ezeket userre külön kezelni?
