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


2024.03.22 konzi

- dataset 20009 -re befejezés
- model átfutása
- megvalósítás elkezdése

2024.03.26 - self notes

model breakdown:

- pre-processed data to a CNN (convolutional neural network)
- mulit-layer neural network - deep supervised learning arch
- CNN = feature extractor + trainable classifier 
- only feature extraction needed: 
    - convolutional filtering
        - unique filters that can detect several features
    - downsampling operations
- CNN 1D

1D convolutional layers:

The convolutional layers define filters or feature detectors with a height equal to the kernel size.
However, signatures are very complex, hence, in each layer, n (which is different in each layer) filters are defined. 
Hence the output of this layer is a m x n where m is the number of points in a signature file - 20 + 1. With the defined kernel size and considering the length of the input matrix, each filter will contain m weights.

algorithm explanation:

![image](/images/1D%20convolution%20algorithm.png)

Convolutions in 1D link: https://www.algorithm-archive.org/contents/convolutions/1d/1d.html

1D max pooling layer:
the layer applies a transformation that maintains the mean activation close to 0 and the activation standard deviation close to 1. greatly accelerates the learning rates. deep neural networks with sigmoid activations

pooling layers: reduce the dimensions of data combining the outputs of neuron clusters at one layer into a single neuron in the next layer, max pooling needed.
pooling: form of linear downsampling.

The pooling layer serves to progressively reduce the spatial size of the representation, to reduce the number of parameters, memory footprint and amount of computation in the network, and hence to also control overfitting. This is known as down-sampling.
A very common form of max pooling is a layer with filters of size 2×2, applied with a stride of 2, which subsamples every depth slice in the input by 2 along both width and height, discarding 75% of the activations:

![image](/images/max%20pooling.png)

maxpooling explained:

![image](/images/max%20pooling%20explained.png)

ReLu layer (rectified linear unit):

applies non-saturating activation function f(x) = max(0,x)
removes negative values from an activation map by setting them to zero

Dropout layer:

randomly assigns 0 weights to neurons in the model. makes the model less sensitive towards smaller variations in the data.

Dropout layer explained:

![image](/images/dropout%20layer.png)

Masking layer:

mask out the padded sequences so that the model doesn't use the padding as features and only predicts on the correct length
of the sample

Masking layer explained:

![image](/images/masking%20layer.png)

Simple RNN layer:

fully connected RNN where the output is to be fed back to the input

Simple RNN layer explained:

![image](/images/simple%20RNN%20layer.png)

Dense layer:

reduce the height of the vector to 4 then 2, using matrix multiplication

Dense layer explained:

![images](/images/dense%20layer%20.png)


Keras library: powerful and easy-to-use free open source Python library for developing and evaluating deep learning models



2024.03.27 - konzi

sigcomp 2009 - training - training and testing (alairokat osztjuk el 80-20 ba ) 5-5 hamisitott es eredeti traininghez, 8 user traininghez 4 ember testinghez(tanitason belul megnezzuk hol tartunk) 
nfi - teszteleshez 5-5/ user

evaluationbe a 20 %, es sgcompbol nfi 
svc bol 40 - 80/20 ba a usereket 


dataset teljesen elokeszitve szunet utanra

tutorial 1d konvolucioshalo tensorban 
szintaktika - layerhozzaadasara 

2024.05.02 - munka

- folderek újratöltése: 
    - svc2004 ből 35 user training/tesing 15/5 ös arányban - high testing accuracy - low evaluation accuracy ~0.785- 0.629 (volt ilyen is: 0.85-0.495), utolsó conv1d kernel size 2->5 - 0.81-0.575
    - Adam = 0.01-re 0.85- 0.6
    - hozzáadva a sigcomp training set - szignifikánsan rosszabb eredmények - low - low accuracy ~0.5

    - binary - sigmoid, sparse categorical - softmax 


2024.05.03 - konzi

- training validation userek nem szetbontasa hogy a tultanulast elkeruljuk
- masik loss function hasznalata


2024.05.03 - munka

84% evaluation accuracy eachieved at 32 batch size, 100 epochs
![images](/images/accuracy.PNG)