#!/usr/bin/env sage

import sys
from sage.all import *

F = FiniteField(101) # Construct finite field
P = F['x'] # Polynomial ring

generate_points = 1
single_poly = 0
adding_shares_linearity = 1
adding_constant_linearity = 1
multiplying_constant_linearity = 1
multiplying_shares_nonlinearity = 1
multiplication_subprotocol = 1
beavers_triple=1


if generate_points:
    print "Creating points for the curve 5x^2 + 10x + 56 and reconstructing from shares:"
    print "=============================================================================="
    f_a = P("56 + 10x + 5x^2")
    shares_a = []
    for i in range(1,4):
        shares_a.append((i,f_a(i)))
    print "Shares of a:",shares_a
    f_a_rec = P.lagrange_polynomial(shares_a)
    print "f_a_rec(x) = ",f_a_rec
    print "Secret = f_a_rec(0) = ",f_a_rec(0)

if single_poly:
    # How to use P:
    original_polynomial = P("56 + 10x + 5x^2")
    # Convert the shares to elements of F (otherwise lagrange_polynomial will fail)
    shares = [(F(x), F(y)) for x,y in [(25, 98), (47, 57), (19, 31)]]
    # Now lagrange_polynomial works fine
    reconstructed_polynomial = P.lagrange_polynomial(shares)
    
    print "Correct reconstruction!" if reconstructed_polynomial == original_polynomial else "Something wrong!"
    print shares
    print "p(x) =", reconstructed_polynomial
    print "Secret = p(0) =", reconstructed_polynomial(0)

if adding_shares_linearity:
    F = FiniteField(101) # Construct finite field
    P = F['x'] # Polynomial ring

    print "Adding shares of 2 and 4:"
    print "=========================="
    f_a = P("2 + x");    f_b = P("4 + x");    f_c = P("4 + 2x") 
    shares_a = [];       shares_b = [];       shares_c = []
    for i in range(1,4):
        shares_a.append((i,f_a(i)))
        shares_b.append((i,f_b(i)))
        shares_c.append((i,f_a(i)+f_b(i)))
    print "Shares_a", shares_a,"\nShares_b",shares_b,"\nShares_c",shares_c
    f_a_rec = P.lagrange_polynomial(shares_a)
    f_b_rec = P.lagrange_polynomial(shares_b)
    f_c_rec = P.lagrange_polynomial(shares_c)
    print "f_a_rec(x) = ",f_a_rec, "\tSecret = f_a_rec(0) = ",f_a_rec(0)
    print "f_b_rec(x) = ",f_b_rec, "\tSecret = f_b_rec(0) = ",f_b_rec(0)
    print "f_c_rec(x) = ",f_a_rec, "\tSecret = f_c_rec(0) = ",f_c_rec(0)

if adding_constant_linearity:
    F = FiniteField(101) # Construct finite field
    P = F['x'] # Polynomial ring

    print "Adding constant 10 to the shares of 2:"
    print "======================================="
    f_a = P("2 + x");    f_b = P("4 + x");
    shares_a = [];       shares_b = [];
    for i in range(1,4):
        shares_a.append((i,f_a(i)))
        shares_b.append((i,f_a(i)+10))
    print "Shares_a", shares_a,"\nShares_b",shares_b
    f_a_rec = P.lagrange_polynomial(shares_a)
    f_b_rec = P.lagrange_polynomial(shares_b)
    print "f_a_rec(x) = ",f_a_rec, "\tSecret = f_a_rec(0) = ",f_a_rec(0)
    print "f_b_rec(x) = ",f_b_rec, "\tSecret = f_b_rec(0) = ",f_b_rec(0)

if multiplying_constant_linearity:
    F = FiniteField(101) # Construct finite field
    P = F['x'] # Polynomial ring

    print "Multiplying constant 4 to the shares of 2:"
    print "==========================================="
    f_a = P("2 + x");    f_b = P("4 + x");
    shares_a = [];       shares_b = [];
    for i in range(1,4):
        shares_a.append((i,f_a(i)))
        shares_b.append((i,f_a(i)*4))
    print "Shares_a", shares_a,"\nShares_b",shares_b
    f_a_rec = P.lagrange_polynomial(shares_a)
    f_b_rec = P.lagrange_polynomial(shares_b)
    print "f_a_rec(x) = ",f_a_rec, "\tSecret = f_a_rec(0) = ",f_a_rec(0)
    print "f_b_rec(x) = ",f_b_rec, "\tSecret = f_b_rec(0) = ",f_b_rec(0)

if multiplying_shares_nonlinearity:
    F = FiniteField(101) # Construct finite field
    P = F['x'] # Polynomial ring

    print "Multiplying shares of 2 and 4:"
    print "==========================================="
    f_a = P("2 + x");    f_b = P("4 + x");    f_c = P("4 + 2x") 
    shares_a = [];       shares_b = [];       shares_c = []
    for i in range(1,4):
        shares_a.append((i,f_a(i)))
        shares_b.append((i,f_b(i)))
        shares_c.append((i,f_a(i)*f_b(i)))
    print "Shares_a", shares_a,"\nShares_b",shares_b,"\nShares_c",shares_c
    f_a_rec = P.lagrange_polynomial(shares_a)
    f_b_rec = P.lagrange_polynomial(shares_b)
    f_c_rec = P.lagrange_polynomial(shares_c)
    print "f_a_rec(x) = ",f_a_rec, "\tSecret = f_a_rec(0) = ",f_a_rec(0)
    print "f_b_rec(x) = ",f_b_rec, "\tSecret = f_b_rec(0) = ",f_b_rec(0)
    print "f_c_rec(x) = ",f_c_rec, "\tSecret = f_c_rec(0) = ",f_c_rec(0)
    print "f_c_rec's factors are ",f_c_rec.factor()

if multiplication_subprotocol:
    F = FiniteField(5) # Construct finite field
    P = F['x'] # Polynomial ring

    print "Multiplying shares of 2 and 2 in multiplication subprotocol:"
    print "============================================================="
    f_a = P("2 + x");    f_b = P("2 +2x");    f_c = P("4 + 2x") 
    shares_a = [];       shares_b = [];       shares_c = []

    f_c1 = P("2 + x");    f_c2 = P("4");        f_c3 = P("4x") 
    shares_c1 = [];       shares_c2 = [];       shares_c3 = [];     shares_C = []

    rec_vector = []
    for i in range(1,4):
        num = 1; denom = 1
        for k in range(1,4):
            if i is not k:
                num = num * -k;   denom = denom * (i-k);
        tmp = num / denom
        rec_vector.append((P(i),P(tmp)))
    print "Reconstruction vector:", rec_vector

    for i in range(1,4):
        shares_a.append((P(i),f_a(i)))
        shares_b.append((P(i),f_b(i)))
        shares_c.append((P(i),f_a(i)*f_b(i)))

    print "Shares_a", shares_a,"\nShares_b",shares_b,"\nShares_c",shares_c

    f_a_rec = P.lagrange_polynomial(shares_a)
    f_b_rec = P.lagrange_polynomial(shares_b)
    f_c_rec = P.lagrange_polynomial(shares_c)
    print "f_a_rec(x) = ",f_a_rec, "\tSecret = f_a_rec(0) = ",f_a_rec(0)
    print "f_b_rec(x) = ",f_b_rec, "\tSecret = f_b_rec(0) = ",f_b_rec(0)
    print "f_c_rec(x) = ",f_c_rec, "\tSecret = f_c_rec(0) = ",f_c_rec(0)
    print "f_c_rec's factors are ",f_c_rec.factor()

    for i in range(1,4):
        shares_c1.append((P(i),f_c1(i)))
        shares_c2.append((P(i),f_c2(i)))
        shares_c3.append((P(i),f_c3(i)))
    print "Shares_c1", shares_c1,"\nShares_c2",shares_c2, "\nShares_c3",shares_c3

    (x,r1) = rec_vector[0]; (x,r2) = rec_vector[1]; (x,r3) = rec_vector[2]
    for i in range(1,4):
        #print f_c1(i),f_c2(i), f_c3(i)
        #print r1, r2, r3
        #print f_c1(i)*r1 + f_c2(i)*r2 + f_c3(i)*r3
        val = f_c1(i)*r1 + f_c2(i)*r2 + f_c3(i)*r3
        shares_C.append((P(i),val))
    print "Shares_C",shares_C

    f_C_rec = P.lagrange_polynomial(shares_C)
    print "f_C_rec(x) = ",f_C_rec, "\tSecret = f_C_rec(0) = ",f_C_rec(0)

if beavers_triple:
    F = FiniteField(101) # Construct finite field
    P = F['x'] # Polynomial ring

    print "Multiplying shares of 2 and 4 using beavers triple:"
    print "============================================================="
    f_a = P("3 + x");    f_b = P("2 +2x");    f_ab = P("6 + 3x") 
    shares_a = [];       shares_b = [];       shares_ab = []

    f_x = P("2 + x");    f_y = P("4 +2x"); 
    shares_x = [];       shares_y = []; 

    for i in range(1,4):
        shares_a.append((P(i),f_a(i)))
        shares_b.append((P(i),f_b(i)))
        shares_ab.append((P(i),f_ab(i)))
        shares_x.append((P(i),f_x(i)))
        shares_y.append((P(i),f_y(i)))

    print "Shares_a", shares_a,"\nShares_b",shares_b,"\nShares_ab",shares_ab
    print "Shares_x", shares_x,"\nShares_y",shares_y

    f_a_rec = P.lagrange_polynomial(shares_a)
    f_b_rec = P.lagrange_polynomial(shares_b)
    f_x_rec = P.lagrange_polynomial(shares_x)
    f_y_rec = P.lagrange_polynomial(shares_y)
    f_ab_rec = P.lagrange_polynomial(shares_ab)
    print "f_a_rec(x) = ",f_a_rec, "\tSecret = f_a_rec(0) = ",f_a_rec(0)
    print "f_b_rec(x) = ",f_b_rec, "\tSecret = f_b_rec(0) = ",f_b_rec(0)
    print "f_ab_rec(x) = ",f_ab_rec, "\tSecret = f_ab_rec(0) = ",f_ab_rec(0)
    print "f_x_rec(x) = ",f_x_rec, "\tSecret = f_x_rec(0) = ",f_x_rec(0)
    print "f_y_rec(x) = ",f_y_rec, "\tSecret = f_y_rec(0) = ",f_y_rec(0)

    shares_alpha_t = [];   shares_beta_t = [];
    for i in range(1,4):
        (x,xi) = shares_x[i-1]; (x,yi) = shares_y[i-1]
        (x,ai) = shares_a[i-1]; (x,bi) = shares_b[i-1]
        shares_alpha_t.append((P(i),xi-ai))
        shares_beta_t.append((P(i),yi-bi))
    print "Shares_alpha_t", shares_alpha_t,"\nShares_beta_t",shares_beta_t
    
    f_alpha_rec = P.lagrange_polynomial(shares_alpha_t)
    f_beta_rec = P.lagrange_polynomial(shares_beta_t)
    alpha = f_alpha_rec(0); beta = f_beta_rec(0)

    print "Alpha = ",alpha,"\tBeta = ",beta;

    shares_xy = []
    for i in range(1,4):
        (x,ab) = shares_ab[i-1]; (x,ai) = shares_a[i-1]; (x,bi) = shares_b[i-1]
        val = ab + alpha*bi + beta*ai + alpha*beta
        shares_xy.append((P(i),val))
    print "Shares_xy", shares_xy

    f_xy_rec = P.lagrange_polynomial(shares_xy)
    print "f_xy_rec(x) = ",f_xy_rec, "\tSecret = f_xy_rec(0) = ",f_xy_rec(0)

