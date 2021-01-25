E = float(input("What is the isotropic Young's Modulus of your material, E in MPa?"))
v = float(input("What is the isotropic Poisson's ratio for your material, v "))

# just taking biaxial stress states atm so assuming s_ij = 0 
components = input("").split(" ")



def simulate_measurements(E,v,components):
# take in macroscopic constants and stress true tensor components
    h3 = 0 # for large 2theta, we can make this assumption
# generate true strain curve 
    for x in range(360):
        for i in components:
            h1 = math.cos(x)
            h2 = math.sin(x)
            
            p_12 = (1/E)*((1+v) ) 
            p_11 = 
        y = 
# add noise to subset of strain to generate strain 'measurements' 
