"""
nth Derivative Calculator - Enhanced Version
This program computes both specific and general nth derivatives symbolically.
"""

import sympy as sp
from sympy import factorial, binomial

def analyze_general_derivative(func, var_symbol, detected_var):
    """
    Analyze and provide general nth derivative formula when possible.
    """
    n = sp.Symbol('n', integer=True, positive=True)
    k = sp.Symbol('k', integer=True, positive=True)
    
    # Compute first several derivatives to detect pattern
    derivatives = [func]
    max_derivs = 10
    
    for i in range(1, max_derivs):
        try:
            derivatives.append(sp.diff(derivatives[-1], var_symbol))
        except:
            break
    
    print("\n" + "=" * 70)
    print("PATTERN ANALYSIS:")
    print("=" * 70)
    
    for i in range(min(8, len(derivatives))):
        if i == 0:
            print(f"f({detected_var})      = {derivatives[i]}")
        else:
            print(f"f^({i})({detected_var})   = {derivatives[i]}")
    
    print("\n" + "=" * 70)
    print("GENERAL nth DERIVATIVE FORMULA:")
    print("=" * 70)
    
    # Analyze the function type
    # 1. Check if polynomial
    if func.is_polynomial(var_symbol):
        degree = sp.degree(func, var_symbol)
        coeffs = sp.Poly(func, var_symbol).all_coeffs()
        
        print(f"\n✓ Polynomial of degree {degree} detected")
        print(f"\nOriginal: f({detected_var}) = {func}")
        print(f"\nGeneral formula:")
        print(f"  • f^(n)({detected_var}) = 0  for n > {degree}")
        
        # For simple power: x^k
        if degree >= 1:
            if len(coeffs) == 2 and coeffs[1] == 0:
                coeff = coeffs[0]
                if coeff == 1:
                    print(f"  • f^(n)({detected_var}) = {degree}!/(({degree}-n)!) × {detected_var}^({degree}-n)  for 0 ≤ n ≤ {degree}")
                else:
                    print(f"  • f^(n)({detected_var}) = {coeff} × {degree}!/(({degree}-n)!) × {detected_var}^({degree}-n)  for 0 ≤ n ≤ {degree}")
        
        print(f"\n  Factorial notation: f^(n)({detected_var}) involves falling factorial")
        
    # 2. Check for exponential e^x or e^(ax)
    elif func == sp.exp(var_symbol):
        print(f"\n✓ Simple exponential e^{detected_var} detected")
        print(f"\nGeneral formula:")
        print(f"  f^(n)({detected_var}) = e^{detected_var}  for all n ≥ 0")
        
    # Check for e^(ax)
    elif func.has(sp.exp):
        args = list(func.atoms(sp.exp))
        if len(args) == 1:
            exp_arg = list(args)[0].args[0]
            if exp_arg.is_polynomial(var_symbol) and sp.degree(exp_arg, var_symbol) == 1:
                coeff = sp.LC(exp_arg, var_symbol)
                print(f"\n✓ Exponential e^({exp_arg}) detected")
                print(f"\nGeneral formula:")
                print(f"  f^(n)({detected_var}) = {coeff}^n × e^({exp_arg})  for all n ≥ 0")
    
    # 3. Check for trigonometric
    elif func == sp.sin(var_symbol):
        print(f"\n✓ Simple sine function detected")
        print(f"\nGeneral formula:")
        print(f"  f^(n)({detected_var}) = sin({detected_var} + nπ/2)")
        print(f"\n  Pattern (cycles every 4):")
        print(f"    n ≡ 0 (mod 4): sin({detected_var})")
        print(f"    n ≡ 1 (mod 4): cos({detected_var})")
        print(f"    n ≡ 2 (mod 4): -sin({detected_var})")
        print(f"    n ≡ 3 (mod 4): -cos({detected_var})")
        
    elif func == sp.cos(var_symbol):
        print(f"\n✓ Simple cosine function detected")
        print(f"\nGeneral formula:")
        print(f"  f^(n)({detected_var}) = cos({detected_var} + nπ/2)")
        print(f"\n  Pattern (cycles every 4):")
        print(f"    n ≡ 0 (mod 4): cos({detected_var})")
        print(f"    n ≡ 1 (mod 4): -sin({detected_var})")
        print(f"    n ≡ 2 (mod 4): -cos({detected_var})")
        print(f"    n ≡ 3 (mod 4): sin({detected_var})")
    
    # 4. Check for logarithm
    elif func == sp.log(var_symbol):
        print(f"\n✓ Natural logarithm detected")
        print(f"\nGeneral formula:")
        print(f"  f^(n)({detected_var}) = (-1)^(n-1) × (n-1)! / {detected_var}^n  for n ≥ 1")
        print(f"  f^(0)({detected_var}) = ln({detected_var})")
    
    # 5. Check for 1/x
    elif func == 1/var_symbol:
        print(f"\n✓ Reciprocal function 1/{detected_var} detected")
        print(f"\nGeneral formula:")
        print(f"  f^(n)({detected_var}) = (-1)^n × n! / {detected_var}^(n+1)  for n ≥ 0")
    
    # 6. Check for x^k (with symbolic k)
    elif len(func.free_symbols) > 1:
        print(f"\n✓ Function with multiple variables detected")
        print(f"\nFor power function {detected_var}^k:")
        print(f"  f^(n)({detected_var}) = k(k-1)(k-2)...(k-n+1) × {detected_var}^(k-n)")
        print(f"               = [k!/(k-n)!] × {detected_var}^(k-n)")
        print(f"               = P(k,n) × {detected_var}^(k-n)")
        print(f"\n  where P(k,n) is the falling factorial (Pochhammer symbol)")
    
    else:
        print(f"\n✓ Complex function detected")
        print(f"\nGeneral formula requires advanced techniques:")
        print(f"  • Leibniz rule for products")
        print(f"  • Chain rule for compositions")
        print(f"  • Faà di Bruno's formula for nested functions")
        print(f"\nPlease observe the pattern above to infer the formula.")
    
    # Additional information
    print("\n" + "=" * 70)
    print("ADDITIONAL FORMULAS:")
    print("=" * 70)
    print(f"\nCommon general derivatives:")
    print(f"  • (x^k)^(n)     = k!/(k-n)! × x^(k-n)")
    print(f"  • (e^x)^(n)     = e^x")
    print(f"  • (e^ax)^(n)    = a^n × e^(ax)")
    print(f"  • (ln x)^(n)    = (-1)^(n-1) × (n-1)!/x^n  [n≥1]")
    print(f"  • (sin x)^(n)   = sin(x + nπ/2)")
    print(f"  • (cos x)^(n)   = cos(x + nπ/2)")
    print(f"  • (1/x)^(n)     = (-1)^n × n!/x^(n+1)")
    
    print("=" * 70)

def compute_nth_derivative():
    """
    Main function to compute nth derivative of a user-provided function.
    """
    print("=" * 70)
    print("          ENHANCED nth DERIVATIVE CALCULATOR")
    print("=" * 70)
    print("\nThis program computes derivatives symbolically.")
    print("\nSupported variables: x, y, z, a, b, c, t, k")
    print("Supported functions: sin, cos, tan, exp, log, sqrt, etc.")
    print("\nExamples:")
    print("  - x**2 + 3*x + 5")
    print("  - a**3")
    print("  - sin(x)")
    print("  - exp(x)")
    print("  - log(x)")
    print("  - 1/x")
    print("=" * 70)
    
    # Get the function from user
    func_str = input("\nEnter your function f(x): ").strip()
    
    # Detect which variable is being used
    possible_vars = ['x', 'y', 'z', 'a', 'b', 'c', 't', 'k']
    detected_var = None
    
    for var in possible_vars:
        if var in func_str:
            detected_var = var
            break
    
    if detected_var is None:
        print("\nError: Could not detect variable. Please use x, y, z, a, b, c, t, or k.")
        return
    
    var_symbol = sp.Symbol(detected_var)
    
    try:
        func = sp.sympify(func_str)
        print(f"\nParsed function: f({detected_var}) = {func}")
        
        # Ask user what they want
        print("\n" + "=" * 70)
        print("OPTIONS:")
        print("=" * 70)
        print("1. Compute specific nth derivative (e.g., n=2, n=5)")
        print("2. Analyze general nth derivative formula (symbolic n)")
        print("3. Both (specific value + general formula)")
        
        choice = input("\nChoose option (1, 2, or 3): ").strip()
        
        if choice == '2':
            # General formula only
            analyze_general_derivative(func, var_symbol, detected_var)
            
        elif choice == '1':
            # Specific value only
            n = int(input(f"\nEnter the order of derivative (n): ").strip())
            
            if n < 0:
                print("\nError: n must be a non-negative integer.")
                return
            
            derivative = func
            for i in range(n):
                derivative = sp.diff(derivative, var_symbol)
            
            print("\n" + "=" * 70)
            print("RESULT:")
            print("=" * 70)
            print(f"Original: f({detected_var}) = {func}")
            
            if n == 0:
                print(f"\n0th derivative = {derivative}")
            elif n == 1:
                print(f"\n1st derivative = {derivative}")
            elif n == 2:
                print(f"\n2nd derivative = {derivative}")
            elif n == 3:
                print(f"\n3rd derivative = {derivative}")
            else:
                print(f"\n{n}th derivative = {derivative}")
            
            simplified = sp.simplify(derivative)
            if simplified != derivative:
                print(f"\nSimplified: {simplified}")
            
            print("=" * 70)
            
        elif choice == '3':
            # Both
            n = int(input(f"\nEnter specific value of n: ").strip())
            
            if n < 0:
                print("\nError: n must be a non-negative integer.")
                return
            
            derivative = func
            for i in range(n):
                derivative = sp.diff(derivative, var_symbol)
            
            print("\n" + "=" * 70)
            print(f"SPECIFIC RESULT (n={n}):")
            print("=" * 70)
            print(f"f^({n})({detected_var}) = {derivative}")
            
            simplified = sp.simplify(derivative)
            if simplified != derivative:
                print(f"Simplified: {simplified}")
            
            # Now show general formula
            analyze_general_derivative(func, var_symbol, detected_var)
        
        else:
            print("\nInvalid choice.")
            return
            
    except Exception as e:
        print(f"\nError: {str(e)}")
        return
    
    print("\n")
    cont = input("Calculate another derivative? (y/n): ").strip().lower()
    if cont in ['y', 'yes']:
        print("\n" * 2)
        compute_nth_derivative()

def main():
    try:
        compute_nth_derivative()
    except KeyboardInterrupt:
        print("\n\nProgram terminated.")
    except Exception as e:
        print(f"\nError: {str(e)}")

if __name__ == "__main__":
    main()