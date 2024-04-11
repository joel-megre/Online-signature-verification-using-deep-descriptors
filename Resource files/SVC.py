from sig2class import Signature as svc
from Sampler import Sampler as smp

path_training = 'C:\\Users\\ASUS\\Documents\\BME\\6. félév\\Önálló laboratórium\\Signature Verification\\training'

first_user = svc(1,  path_training)

first_signature = first_user.get_signatures(1) #only gives back the data of the first user normalzed
all_signatures = first_user.get_all_signatures() #gives back all the data of the first user normalized

#print(all_signatures)
#print(first_signature)

sampler = smp(path_training)

first = sampler.database['1']['U1S1.txt']
for_users = sampler.database
#print(first)
print(for_users)