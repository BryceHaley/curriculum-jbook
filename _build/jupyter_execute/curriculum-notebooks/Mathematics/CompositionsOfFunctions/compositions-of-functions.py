![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Mathematics/CompositionsOfFunctions/compositions-of-functions.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

# Compositions of Functions

## Compositions of Univariate Functions

Compositions of functions sound a lot worse than they are. The most basic way to describe them is as a "function of a function". As with most mathematical language, that description isn't particularily enlightening. So, let's start with an example, an example so simple it risks annoying a pedantic mathematician. Which is how we know that it is an excellent example. Suppose you have two functions $f(x)$ and $g(x)$ defined as follows

\begin{equation}
 f(x) = x
\end{equation}

and
\begin{equation}
g(x) = 1
\end{equation}

While keeping these simple functions in mind, let's work our way through a few definitions. A composition of functions defined as

\begin{equation}
 f \circ g = f[g(x)]
\end{equation}

where this is read as $f$ of $g$ of $x$. This notation is telling us to write $f(x)$ as a function of $g(x)$, so rather than a function of a variable, it's becoming a function of a function. With the functions above however, this works out to be exactly the same as putting a number into your function, which we see as follows

\begin{equation}
f[g(x)] = \underset{\substack{\downarrow \\ \text{Inserted g(x) at x}}}{g(x)} = 1
\end{equation}

Great, so a composition of functions reduces to the case of inserting a constant in for your variable. But what about if you had more complex functions? Well, consider the functions
\begin{equation}
 f(x) = x + 5
\end{equation}

and

\begin{equation}
g(x) = x^2 -4
\end{equation}

How will we write $f \circ g$ with these functions? It's actually just as simple as putting numbers in for the variables like we saw above, except this time, we'll put the definitions of functions in for each variable. 


\begin{equation}
f[g(x)] =\underset{\substack{\downarrow \\ \text{Inserted g(x) at x}}}{g(x)} + 
\overset{\substack{\text{Constants just hang out} \\ \uparrow} }{5} = 
\underbrace{x^2 - 4}_\text{Insert definition of g(x) for x} + 5 = x^2 + 1
\end{equation}

or going the other direction

\begin{equation}
g[f(x)] = f^2(x) - 4 = (x+5)^2 -4
\end{equation}

where this applies to any composition of functions. To put it simply, if you have a composition of functions all you need to do is place the "inner" function everywhere you see the variable in the "outer" function exactly as you'd put a number into the formula. 

Python provides us with some great tools in order to graph these functions easily. If you have some knowledge of Python you can easily skip this explanation and move right on to the next cell. If not, we're going to take a moment to understand what the code you're about to see does. First up, let's go over the first bit of code you're going to see.
## Digression: Basic Python

### Imports
At the beginning of most Python programs you're more than likely to see a few (or many) `import` statements. The purpose of these is to bring in other pieces of code, that either you or someone else have written, in order to keep your current program more manageable. For example, the set of import statements we're going to use to plot our functions look like this. Select the code cell below then press the `▶Run` button in the toolbar.

#import matplotlib
import matplotlib.pyplot as plt
%matplotlib inline
import numpy as np
print('Libraries succesfully imported.')

Starting from the top down, let's go over what each piece of this code does. 

* **import matplotlib**:  

* **import matplotlib.pyplot as plt**: This command tells Python to import the graphing subroutines from the `matplotlib` package and assign them the name `plt` so we don't have to type as much when we want to produce a graph.

* **%matplotlib inline:** This is specific to Jupyter notebooks. It tells matplotlib to output graphs in the cell directly below the one in which the code is executed. For more information about Jupyter "magic commands" feel free to read [this document](http://ipython.readthedocs.io/en/stable/interactive/magics.html).

* **import numpy as np**: This imports the Python package `numpy` or "numerical Python" and assigns the name to it within our code to `np` so we don't have to type out `numpy` every time we need a function. We'll be using this package for mathematical functions like sine and the square root.

### Plotting

After required modules have been imported into our script, we're ready to get started creating graphs. First up, we need to define a number of points which to plot. It is an unfortunate fact that our computer doesn't know that any variable $x$ is continuous, so we have to create some discrete data with which to plot our functions. We can do that in Python using numpy as follows (Click the next cell and press control and enter at the same time on your keyboard.

x = np.linspace(-3,3,5)
print("x = ", x)

This creates a **list** of numbers called `x` which consists of 5 numbers evenly spaced in the range $[-3,3]$ that we'll use to plot our functions. The `print` function is a standard Python function that simply displays our variables to the screen as either numbers or characters. In order to plot our functions, we type the following. Note that we've increased the number of points in `x` to create a smoother plot. Feel free to change the number `500` to something smaller and observe how the plot changes. 

x = np.linspace(-3,3,500)
plt.plot(x, x**2-4, label='$g(x) = x^2 -4$')

Where there's actually a fair bit in the above line of code that we should take note of. First, by using `plt.plot` we're calling a function from `matplotlib.pyplot` that we called `plt` called `plot`. This function, unsurprisingly, is used to tell Python what to plot. We then pass this function a number of arguments. The first argument `x` is the list of numbers we generated earlier. The second argument `x**2 - 4` is the mathematical function we're going to plot. Here `x` is the variable we're going to plot, and also the list of points that we generated earlier. The `**` is the Python way of "the power of". So, what we're really saying here is $x^2-4$. Finally, the `label='$g(x) = x^2 -4$` is the label we're creating for the plot legend so we can distinguish our plots. The dollar signs are simply formatting so our plot looks nice. 

Now, that graph is missing a lot of the important things like axis labels and a legend. We can add those like this

plt.plot(x, x**2-4, label='$g(x) = x^2 -4$')
plt.xlabel("$x$", fontsize=16)
plt.ylabel("$f(x)$", fontsize=16)
plt.legend()
plt.margins(0)
plt.show()

where the `plt.` calls are still calling functions from `matplotlib.pyplot` however this time we're creating x-axis labels with `plt.xlabel` and y-axis labels with `plt.ylabel`. Finally `plt.legend()` creates the legend for our plot and `plt.show()` displays the plot of our functions. We can also do this all in one cell, rather than breaking it up, as shown below, as well as adding an additional function to plot. 

x = np.linspace(-3,3,500)
plt.plot(x, x**2 - 4, label = '$g(x) = x^2 -4$')
plt.plot(x, x+5, label= '$f(x) = x + 5$')
plt.xlabel("$x$", fontsize=16)
plt.ylabel("$f(x)$ and $g(x)$", fontsize=16)
plt.margins(0)
plt.legend()
plt.show()

We now have two functions: one linear and one parabolic. But what does the composition of these two functions look like? Well, let's use Python to graph their composition! Note that we're adding a few more functions to plot, but the basic plotting is identical. As well, we've already imported the packages we need, so we don't have to do it again! 

### Question:
1. Do you understand what each line of code below is doing?

# Anything in a line of code after a pound sign isn't run, and is known as a comment.

# First let's plot our original functions again
plt.plot(x, x**2 - 4, label = '$g(x) = x^2 -4$')
plt.plot(x, x+5, label= '$f(x) = x + 5$')
# And now the new functions
plt.plot(x, (x+5)**2 - 4, label = '$g[f(x)] = (x+5)^2 - 4$')
plt.plot(x, x**2 + 1, label = '$f[g(x)] = x^2 + 1$')
plt.xlabel("$x$", fontsize=16)
plt.ylabel("Value of Functions of $x$", fontsize=16)
plt.margins(0) # so there is no extra space on the plot
plt.legend()
plt.show()

Where we see from the plot above that depending on the order of the function of functions we get a very different plot! In one case, we have a parabola that shifts up the y-axis by four, and in the other case we get a much wider parabola!

**Do you understand why?**

*Hint: what is the affect of constants on polynomial functions? How about if the constant is inside parentheses?*

## More Complicated Examples

This can also be applied to more complicated compositions of functions. For example, can you have a function of function functions? Absolutely! Like anything in math, you can do whatever you want provided you have the patience to work through it. But just as an example, what if we had three functions, say $f(x)$, $g(x)$ and $h(x)$ which are defined as follows
\begin{equation}
 f(x) = 6\sqrt{x^2 + 1}
 \end{equation}

\begin{equation}
g(x) = 3\sin(\pi x - a)
\end{equation}

\begin{equation}
h(x) = x^3 + x^2
\end{equation}

where $a$ is an arbitrary numerical constant. How would we go about writing $f \circ g \circ h$ ($f$ of $g$ of $h$)? It certainly looks intimidating, but I promise you it looks a lot worse than it actually is. Let's follow our typical PEDMAS rules, in this case, we start with the only thing we have: parenthesis! And, because we have two sets, we start with the inner most set. In this case, let's solve the smaller problem of $g[h(x)]$ where we'll do the same as above, and simply shove $h(x)$ anywhere we see an $x$ in $g(x)$. This is outlined below, however we've dropped some of the explaination with the algebra, but, we're doing absolutely nothing different from what we saw in the previous examples.

\begin{equation}
g[h(x)] = \sin(\pi h(x) - a) = \sin(\pi(x^3 + x^2) - a)
\end{equation}

where we notice that the constant term $a$ simply comes along for the ride. We're half way done! Now that we have an expression for $g[h(x)]$, we can now easily find our complete expression of $f[g[h(x)]]$ in the _exact_ same way we have been doing. 

\begin{equation}
f\circ g \circ\ h= f[g[h(x)]] = \sqrt{g^2[h(x)] + 1} = 6\sqrt{\sin^2[\pi (x^3 + x^2) - a] + 1}
\end{equation}

Where that's a pretty ugly function, but the process of coming to it was not nearly as horrible as that expression looks.

Where we just have to remember our one rule for compositions of univariate functions: shove the inner function anywhere you see the variable in the outer function, exactly as you would shove a number into a formula, and follow PEDMAS rules. 

Let's take a look at how these functions and their compositions look graphically

# Let's start by taking a look at our basic functions

# here np.sqrt is the square root function. 
plt.plot(x,6*np.sqrt(x**2 + 1), label = '$f(x) = 6\sqrt{x^2+1}$')
plt.plot(x, 3 *np.sin(np.pi * x-1), label="$g(x,1) = \sin(\pi x - 1)$")
plt.plot(x, x**3 + x**2, label = "$h(x) = x^3 + x^2$")
plt.xlabel("$x$", fontsize=16)
plt.ylabel("Value of Functions of $x$", fontsize=16)
plt.margins(0)
plt.legend()
plt.show()

Where these functions are certainly a little more exciting than they were before, but in order to plot these compositions of functions, we're going to have to do a lot of typing! Worse than that, a lot of very redundant typing that is prone to error. Is there a better way to plot these functions, that is both more accurate and won't take us as long? The answer is absolutely! We just have to define a function within Python that represents our functions that we wish to plot and compose. 

### Python Digression

In order to define a function in Python we use a key word known as `def`, which for us stands for "define a function". Let's work through the steps we would go through in order to define the function 

\begin{equation}
f(x) = 6\sqrt{x^2 + 1} 
\end{equation}

in Python. We can do this using the following snippet of code

def f(x): 
    return 6 * np.sqrt(x**2 + 1)
print("f(12) =", f(12))

where here we've used the Python keyword `def` and given the function we're defining a name "`f`". We've also told Python that our function named `f` takes one variable as input which we've called "`x`". We also have used keyword `return`, which for us can be though of as an equals sign: we pass a number in to `f` and the function will return what `f` is equal to at that number. Another important thing to notice is that `return` is indented relative to `def`. This is how Python knows that `return` and the statement after are part of the function. Every time you write a function, any code inside it will have to be consistently indented. The choice of function and variable names are completely arbitrary. A function defined like

def A_Really_Bad_Name_For_A_Function_That_Takes_Forever_To_Type(A_Really_Long_Variable_Name):
    return 6 * np.sqrt(A_Really_Long_Variable_Name**2 + 1)

print("A_Really_Bad_Name_For_A_Function_That_Takes_Forever_To_Type(12) =" , 
      A_Really_Bad_Name_For_A_Function_That_Takes_Forever_To_Type(12))

behaves exactly the same as our function `f`. 

Another important fact about functions is that the value we pass this function need not be named `x`. We can pass it a number we've named `NickNackPattyWack` if we wanted to, it will behave the same. Shown explicitly below with a simple example where the functions take a value as input, and return that value divided by ten.

# note: you must always define a function before you use it.

# Check out how this function is written differently but behaves the same.
# Also pay attention to the consistent indentation within the function
def f(x):
    Divisor = 10
    Result = x /10
    return Result

def A_Really_Bad_Name_For_A_Function_That_Takes_Forever_To_Type(A_Really_Long_Variable_Name):
    return A_Really_Long_Variable_Name/10

number = 4
NickNackPattyWack = 4

print("The results are below")
print("f(",number,") =", f(number))
print("f(", NickNackPattyWack, ") =", f(NickNackPattyWack))
print("A_Really_Bad_Name_For_A_Function_That_Takes_Forever_To_Type(", number, ") =",
      A_Really_Bad_Name_For_A_Function_That_Takes_Forever_To_Type(number))
print("A_Really_Bad_Name_For_A_Function_That_Takes_Forever_To_Type(", NickNackPattyWack, ") =",
      A_Really_Bad_Name_For_A_Function_That_Takes_Forever_To_Type(NickNackPattyWack))

Where I've rudely introduced Python's `print` function without telling you about it first. This function outputs numbers and text to the screen. But the point is, that these functions do the same thing even with different names and different numbers. 

As an additional note, what I've shown here is very simple. Python functions can get considerably more involved, as you can have any amount of code between the `def` statement and the `return` statement. A function can do a lot of great things for you, and I'll hopefully touch on that later in an appendix.

Now that we've gone over defining functions, let's define the functions we've specified earlier in this notebook.




def f(x):
    return 6*np.sqrt(x**2 + 1)

# Note here we've given our function an extra argument 'a'
# this is the arbitrary constant we discussed before, but we'll pass it any value we want! 

# np.pi is simply the value of pi, or 3.1415962.... from the numpy package. 
def g(x,a):
    return  3 *np.sin(np.pi * x-a)

def h(x):
    return x**3 + x**2

Great! Let's see if these still look the same if we plot them before moving on to seeing how their compositions look

# Check out how convenient it is to not type our the expression every time!
plt.plot(x,f(x), label = '$f(x) = 6\sqrt{x^2+1}$')

# Also note that we're setting the value of 'a' equal to 1 for this plot. 
plt.plot(x, g(x,a=1), label="$g(x,1) = \sin(\pi x - 1)$")

plt.plot(x,h(x), label = "$h(x) = x^3 + x^2$")
plt.xlabel("$x$", fontsize=16)
plt.ylabel("Value of Functions of $x$", fontsize=16)
plt.margins(0)
plt.legend()
plt.show()

Where the plot above is identical to the one we saw before! It works! Now we'll be able to see the power of both the composition of function notation $f[g(x)]$ and Python functions! 

### Back to the Math

Now that we can make graphs in a more laz... efficient way, let's see what the compositions of these functions look like graphically. There's a handy feature about compositions of functions that behave the same way mathematically in Python as they would if you were to solve the composition by hand. For example, with the Python functions we have defined above, all we need to do to find $f[h(x)]$ where $x=1$ for example is 

number = 1
print("f[h(x)] =",f(h(number)))

Where this follows traditional PEDMAS like rules. Essentially the value of $h(x)$ gets passed in as the variable to $f(x)$ and then it evaluates that new expression at `Number = 1`. This evaluates to the same answer that you would get should you have done the algebra yourself. Let's take a look at how these compositions of functions look like. However we have decreased the range of the function to show from [-3,3] to [-1.5,1.5].

# Look how much easier this is than typing the functions out every time!
plt.plot(x, g(h(x),a=1), label = "$g[h(x),1]= \sin(\pi(x^3 + x^2) - a)$")
plt.xlabel("$x$", fontsize=16)
plt.ylabel("Value of Functions of $x$", fontsize=16)
plt.xlim([-1.5,1.5])
plt.margins(0)
plt.legend()
plt.show()

That function is beginning to look pretty complicated, which is unsurprising considering the non-linearity of the functions we have chosen to combine. However, look how simple that was to plot in Python. Rather than having to solve the composition of functions ourselves, we told Python, we took advantage of Python functions and let the computer to do it for us! Convenient! Let's take a look at how these compositions of functions looking graphically.

plt.plot(x, g(h(x),a=1), label='$g[h(x),1]$')

# We don't need to explicitly state 'a=1', we can put the value in the correct argument location 

plt.plot(x, h(g(x,1)), label = '$h[g(x,1)]$')
plt.plot(x, f(g(x,1)), label= '$f[g(x,1)]$')
plt.plot(x, f(h(x)), label ='$f[h(x)]$')
plt.plot(x, g(f(x),a=1), label ='$g[f(x),1]$')
plt.xlabel("$x$", fontsize=16)
plt.ylabel("Value of functions", fontsize=16)

# This changes the x-axis range
plt.xlim([-1.5,1.5])

# This changes the y-axis range
plt.ylim([-25,50])

# This moves the legend from its default position to something more appropriate
plt.legend(bbox_to_anchor=(1.0, .5))

plt.show()

Where that's pretty cool how easily we can view the graphical behavior of compositions of these functions without defining them explicitly! 
#### Exercise
1. Find (by hand) and plot the resulting function (by defining your own function) of $g[h(x),1]$, does it look like the plot above?

2. Find (by hand) and plot the resulting function (by defining your own function) of  $h[g(x,1)]$, does it look like the plot above?

3. Find (by hand) and plot the resulting function (by defining your own function) of  $f[g(x,1)]$, does it look like the plot above?

4. Find (by hand) and plot the resulting function (by defining your own function) of  $f[h(x)]$, does it look like the plot above?

5. Find (by hand) and plot the resulting function (by defining your own function) of  $g[f(x),1]$, does it look like the plot above?
    


## Operations of Functions

Operations of functions, for practical purposes, mostly a mathematical short hand. It's easier to see and avoid your mistakes by writing as little possible, so operations of functions are simply a small abstraction which prevents you from having to write as many things down, and reducing the chance of making a silly mistake. 

Suppose you want to add two functions together, with as little writing as possible. Well, let's introduce the notation of function operations! Suppose we have two functions

\begin{equation}
f(x) = x^2
\end{equation}

and 

\begin{equation}
g(x) = 2x + 10
\end{equation}

How would we add those together? Certainly we _could_ write 

\begin{equation}
f(x) + g(x) = x^2 + 2x + 10
\end{equation}

but what if those functions were gigantic? In this case we have the following short-hand notation:

\begin{equation}
(f + g)(x) = f(x) + g(x) = x^2 + 2x + 10 
\end{equation}

similarly for subtraction:
\begin{equation}
(f - g)(x) = f(x) - g(x) = x^2 -2x - 10 
\end{equation}

I know what you're thinking: addition and subtraction are great, but I'm a bit of a mathematical sauvant, and I would also like to multiply and divide functions. We'll I've got news for you kiddo: we've got a short-hand for that too.

Multiplication:
\begin{equation}
(f \times g)(x) = f(x)g(x) = x^2(2x + 10)
\end{equation}

Division:
\begin{equation}
\left(\frac{f}{g}\right)(x) = \frac{f(x)}{g(x)} = \frac{x^2}{2x + 10}
\end{equation}

This shorthand behaves exactly like regular math, but you "map" your variable back onto the function afterwards, certainly you could even stop writing the variable completely. Of course, a natural question now arises: how is this useful? Suppose you have three functions 

\begin{aligned}
f(x) = & x^2 \sin^2(x) + x^2 \\
g(x) = & \frac{x^3\log_{10}(x) + 10^x}{10} \\
h(x) = & x^2\cos^2 + x^2
\end{aligned}

First, let's define them in Python so we can observe how these functions behave

def f(x):
    return x**2. * (np.sin(x)**2. + 1.)

def g(x):
    return (x**3. * np.log10(x) + 10.**x)/10.

def h(x):
    return x**2. * (np.cos(x)**2 + 1.)

x = np.linspace(0.01,2.5,1000)
plt.plot(x, f(x), label = "$f(x)$")
plt.plot(x, g(x), label = "$g(x)$")
plt.plot(x, h(x), label = "$h(x)$")
plt.legend()
plt.margins(0)
plt.xlabel("$x$")
plt.ylabel("Functions of $x$")
plt.show()

Where those functions seem to be pretty well behaved. However, what if we wanted to find an expression for 

\begin{equation}
y=\frac{f(x)g(x) + h(x)g(x)}{g(x) \left([f(x) + 1]^2 + [h(x) +1]^2 - f^2(x) - h^2(x) - 2\right)^2}
\end{equation}

where that looks pretty intimidating, I certainly wouldn't want to put the definitions of my functions into the expression for $y$. But, let's use operations of functions to see if we can simplify that expression before we evaluate it.

\begin{aligned}
&\text{Factor the numerator} \\
y &=\frac{g \left(f + h \right)}{g \left([f + 1]^2 + [h +1]^2 - f^2 - h^2 - 2)\right)^2} \\
\\
&\text{Expand denominator} \\
y &=\frac{g \left(f + h \right)}{ g \left(f^2 +2f + 1 + h^2 + 2h + 1 -f^2 -h^2 - 2  \right)^2} \\ \\
&\text{Collect terms and simplify} \\
y & = \frac{f + h}{ (2f + 2h) ^2} = \frac{f+h}{4(f+h)^2} \\ \\
&\text{Cancel common terms}\\
y & = \frac{1}{4}\frac{1}{f + h} \\ \\
&\text{Insert Function definitions}\\
y &= \frac{1}{x^2 \sin^2(x) + x^2 + x^2 \cos^2(x) + x^2} \\ \\
&\text{Simplify} \\
y&=\frac{1}{4}\frac{1}{x^2( \sin^2(x) + \cos^2(x) + 2)} \\ \\
&\text{Pythagorean Theorem} \\
y&= \frac{1}{12x^2}
\end{aligned}

While we still had to do a little algebra, by using operations of functions we saved ourselves a considerable amount of time working through that simplification, and in fact found that our solution didn't depend on $g(x)$ at all! Although that looks all too convenient, let's test if this lines up using Python to double check our expression. First, let's define a helper function to handle that nasty composition of functions. 

def comp(x):
    numerator = g(x)*(f(x) + h(x))
    denominator = (f(x) + 1.)**2. + (h(x) + 1. )**2. - f(x)**2. - h(x)**2. - 2.
    denominator = g(x) * denominator**2.
    return numerator/denominator

def simplified(x):
    return 1. /(12.* x **2.)

x = np.linspace(0.5,10,1000)
plt.plot(x, comp(x), label = "comp")
plt.plot(x, simplified(x), label = "Simplified")
plt.legend()
plt.xlabel("$x$")
plt.ylabel("Function Value")
plt.show()

Where that looks pretty exact! But, if Python is happy to use our unsimplified functions, why bother with all that algebra in the first place? Well, let's take a look at how long it takes to make that calculation using each function. Run the cell below to time how long it takes each function to calculate a number. Note this cell takes some time to run. 

# import the time library
import time

# create empty lists we'll use for plotting
x_points = []
y_points = []

# This runs the code below it 100 times, from i=1 to i=99
for i in range(1, 100):
    # Record current time
    start1 = time.time()
    for b in range(i * 100):
        a = comp(i)
    # record end time
    end1 = time.time()
    
    # calculate total time
    total1 = end1 - start1
    
    # time our second function
    start = time.time()

    for b in range(i * 100):
        a = simplified(i)
    
    end = time.time()
    total2 = end - start
    x_points.append(total1/total2)
    y_points.append(i* 100)
    
plt.plot(x_points,y_points)
plt.xlabel("Ratio of time spent between the simplified and composite function")
plt.ylabel("Number of Points Calculated")

Where we see that the unsimplified function is about _fifty times_ slower than our simplified version. This is very important in many computations because you don't want to spend too long waiting for an answer. So even though your computer will calculate the value of a composition of functions, knowing how to simplify those functions by hand is still incredibly important. 

## Conclusion

In summary, operations of functions come down to making a substitution: rather than manipulating the variables individually, we manipulate the entire function first to see if we can make things easier on ourselves. We can also use those compositions of functions to visualize them well in Python and observe their complex behaviour. While a lot of the time they look complicated, the process deriving the composition of functions is not very difficult.



## Real Life Examples

Compositions of functions are used everyday in physics and engineering. Have you ever made a substitution in your analysis? Well, then you've been using compositions of functions! Let's work through an example. For example, let's say we wanted to calculate the kinetic energy of an object undergoing uniform circular motion. I state without proof that the formula for kinetic energy is 

$T(v) = \frac{1}{2} m v^2.$

Where $T$ is the kinetic energy, $v$ is the _velocity_ of the object, and $m$ is its mass. For circular motion the formula for velocity is 

$v(\omega) = \omega R,$

where $\omega$ is the angular velocity, or how quickly the angle changes as a function of time, and $R$ is the radius of the circle. If you wanted to get the kinetic energy of a particle in uniform circular motion, we do what we've already been doing! Composition of functions, looking for $T(v(\omega))$, or the kinetic energy as a function of angular velocity (or kinetic energy of velocity of angular velocity). 

$T(v(\omega)) = \frac{1}{2} m \left(\omega R \right)^2 = \frac{1}{2} m \omega^2 R^2.$

Essentially, if you ever hear the phrase "make a substitution" you should be thinking "composition of functions".

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)