![Callysto.ca Banner](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-top.jpg?raw=true)

<a href="https://hub.callysto.ca/jupyter/hub/user-redirect/git-pull?repo=https%3A%2F%2Fgithub.com%2Fcallysto%2Fcurriculum-notebooks&branch=master&subPath=Mathematics/HorizontalAndVerticalTranslations/effects-of-horizontal-and-vertical-translations.ipynb&depth=1" target="_parent"><img src="https://raw.githubusercontent.com/callysto/curriculum-notebooks/master/open-in-callysto-button.svg?sanitize=true" width="123" height="24" alt="Open in Callysto"/></a>

%%html

<script>
  function code_toggle() {
    if (code_shown){
      $('div.input').hide('500');
      $('#toggleButton').val('Show Code')
    } else {
      $('div.input').show('500');
      $('#toggleButton').val('Hide Code')
    }
    code_shown = !code_shown
  }

  $( document ).ready(function(){
    code_shown=false;
    $('div.input').hide()
  });
</script>
<p> Code is hidden for ease of viewing. Click the Show/Hide button to see. </>
<form action="javascript:code_toggle()"><input type="submit" id="toggleButton" value="Show Code"></form>

import numpy as np
import ipywidgets as widgets
from plotly import graph_objs as go

# Horizontal and vertical translations

This notebook introduces the topic of translating a function both vertically and horizontally. Although this may sound hard, all it really means is that we can move the graph of a function up and down (vertically) and from side to side (horizontally). By the end of this lesson, you will better understand what it means to translate a function, how a translation affects the function's graph, and how a translation affects the equation that defines the function.

## Background and simple example

Translations are used in many mathematical applications. When a function is translated, either horizontally or vertically, we get a new function. Let's start with a  simple example.

Take the equation $y=x^2$, which is the formula for a parabola. We can graph it by plotting a series of x values horizontally, paired with the square of those values vertically. You will get the following graph:



x = np.linspace(-4,4,200)
fig = go.Figure(data = go.Scatter(x = x, y = x**2))
fig.update_layout(title='A parabola, y=x^2',
                   xaxis_title='x values',
                   yaxis_title='y values')
fig.show()

Notice, for instance, the point $x=4$ has square $y = 4^2 = 16$ and the parabola does indeed pass through the point $(x,y) = (4,16).$

#### Vertical shift

To shift this graph upwards (vertically), say by five, we just add 5 to the function $x^2$:

x = np.linspace(-4,4,200)
fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=x**2,
                    mode='lines',
                    name='original'))
fig.add_trace(go.Scatter(x=x, y=x**2 + 5,
                    mode='lines',
                    name='vertical shift'))

fig.update_layout(title='A parabola, y=x^2, and shifted up, y=x^2 + 5',
                   xaxis_title='x values',
                   yaxis_title='y values')
fig.show()

#### Horizontal shift

To shift this graph to the right (horizontally), say by two, we just **subtract** 2 from the x in  function $x^2$, to get $y = (x-2)^2$:

x = np.linspace(-4,6,200)
fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=x**2,
                    mode='lines',
                    name='original'))
fig.add_trace(go.Scatter(x=x, y=(x-2)**2,
                    mode='lines',
                    name='horizontal shift'))

fig.add_trace(go.Scatter(x=[0], y=[0],
                    mode='markers',
                    name='original vertex'))

fig.add_trace(go.Scatter(x=[2], y=[0],
                    mode='markers',
                    name='shifted vertex'))

fig.update_layout(title='A parabola, y=x^2, and shifted right,  y=(x-2)^2',
                   xaxis_title='x values',
                   yaxis_title='y values')
fig.show()

## Ask yourself

Notice to raise the function up, we added 5 to $x^2$. To move the function to the right, we **subtracted** 2 from the x variable, $x^2$ become $(x-2)^2$. Does this make sense to you?

If not, think about moving the vertex of the parabola to the right. To move it from (0,0) to (2,0), we need the squaring function to have a minimum at $x=2$. The function $(x-2)^2$ does have its minimum at 2, as desired. 

## Application example

Think about throwing a ball up in the air. Imagine you are being timed by your friend, and that you throw the ball in the air as soon as your friend says 'Go'. If we drew a graph of how high the ball goes over time, the graph might look something like this:

# This code to be hidden.
x = np.linspace(0,2,200)

t1 = go.Scatter(
    x = x,
    y = -5*(x-1)**2 + 5, 
    mode='lines',name='path')

fig = go.Figure()
fig.add_trace(t1)
fig.update_layout(title='Parabolic path of a thrown ball',
                   xaxis_title='Time (seconds)',
                   yaxis_title='Height (meters)')
fig.show()

There's something wrong with this graph, though. At time 0, when you throw the ball, the ball has a height of 0 meters. So this graph is saying that you threw the ball from the ground, i.e. your hand was on the ground when you threw the ball. This is completely impossible, so we'll adjust the graph. Let's say that, with your arm extended above your head, you're about 2.2 m tall. To make things easier, let's imagine that you throw the ball with your arm fully extended and you catch the ball with your arm fully extended. The graph of the height of the ball over time should now look like this: 

# This code to be hidden.
x = np.linspace(0,2,200)
t1 = go.Scatter(
    x = x,
    y = -5*(x-1)**2 + 5 + 2.2,
    mode='lines',
    name='path'
)

fig = go.Figure()
fig.add_trace(t1)
fig.add_trace(go.Scatter(x=[0], y=[0], mode='markers',name='origin'))
fig.update_layout(title='Parabolic path of a thrown ball, shifted up a bit',
                   xaxis_title='Time (seconds)',
                   yaxis_title='Height (meters)')
fig.show()

Alright, now this makes a bit more sense. The ball starts at height 2.2 m, is in the air for 2 seconds, and then you catch it when it is 2.2 m high.

What we've just seen is a *vertical* translation, since the graph of the ball's height got moved *up*.

Now let's imagine that you throw and catch the ball at the same height, but when your friend says 'Go' you wait for 1 second to throw the ball. The graph of the height of the ball now looks like this:

# This code to be hidden.
x = np.linspace(0,2,200)
t1 = go.Scatter(
    x = x + 1,
    y = -5*(x-1)**2 + 5 + 2.2)

fig = go.Figure()
fig.add_trace(t1)
fig.add_trace(go.Scatter(x=[0], y=[0], mode='markers',name='origin'))
fig.update_layout(title='Parabolic path of a thrown ball, shifted up and to the right',
                   xaxis_title='Time (seconds)',
                   yaxis_title='Height (meters)')
fig.show()

This is the same graph as before, but it's been moved to the *right*. This is a *horizontal* translation. Just for comparison, let's see all three graphs together.

# Hide this.
x = np.linspace(0,2,200)
t1 = go.Scatter(
    x = x,
    y = -5*(x-1)**2 + 5,
    name = 'Original path')

t2 = go.Scatter(
    x = x,
    y = -5*(x-1)**2 + 5 + 2.2,
    name = 'Path translated up')

t3 = go.Scatter(
    x = x + 1,
    y = -5*(x-1)**2 + 5 + 2.2,
    name = 'Path translated up and to the right')

fig = go.Figure()
fig.add_trace(t1)
fig.add_trace(t2)
fig.add_trace(t3)
fig.add_trace(go.Scatter(x=[0], y=[0], mode='markers',name='origin'))
fig.update_layout(title='Parabolic paths of three thrown balls',
                   xaxis_title='Time (seconds)',
                   yaxis_title='Height (meters)')
fig.show()

## Checking In

After seeing the example of throwing the ball into the air, see if you can answer these questions. 

-  How does a **vertical** translation affect the graph of a function? 
-  How does a **horizontal** translation affect the graph of a function? 
-  What other real-world application could use translations? 


You've seen an example of how translations affect the *graph* of a function, now let's talk about how translations affect the *equation* of a function. This can get tricky, so it's important to imagine the graph of the function moving around as we apply translations.

### More examples

Let's look at the function $f(x) = x$. The graph of this function is a diagonal line. Let's take a look.

# Create the x and y variables for plotting the function.
x = np.linspace(-10,10,200)

# Assign the variables for plotting.
f_graph = go.Scatter(
    x = x,
    y = x,
    name = 'f(x)')

# Assign the plot to a figure.
fig = go.Figure(f_graph)

# Plot the function.
fig.update_layout(title='Plot of a diagonal line',
                   xaxis_title='x values',
                   yaxis_title='y = f(x)')
fig.show()

You can move your mouse cursor over the graph to get some values of the function. Let's write some values down in a table.   

$$
\begin{array}{c|c}
x & y=f(x) \\ \hline
-2 & -2 \\
-1 & -1 \\ 
0 & 0 \\
1 & 1 \\
2 & 2
\end{array}
$$

Now what would happen if we added 2 to every $y$ value? For one thing, the table would now look like this:

$$
\begin{array}{c|c}
x & y=f(x) + 2 \\ \hline
-2 & -2 + 2 = 0 \\
-1 & -1 + 2 = 1 \\ 
0 & 0 + 2 = 2 \\
1 & 1 + 2 = 3 \\
2 & 2 + 2 = 4
\end{array}
$$

Now how does that affect the graph? Let's plot it to find out.

x = np.linspace(-10,10,200)

# Two traces for plotting.
f_graph = go.Scatter(
    x = x,
    y = x,
    name = 'f(x)')
f_translated = go.Scatter(
    x = x,
    y = x+2,
    name = 'f(x) + 2')

data = [f_graph, f_translated]

fig = go.Figure([f_graph,f_translated])
fig.update_layout(title='Plot of two diagonal lines: y = x and y = x + 2',
                   xaxis_title='x values',
                   yaxis_title='y = f(x), y = f(x) + 2')
fig.show()

From this graph, we can see that adding 2 to every $y$-value moved the graph of $f(x)$ up 2 units.

Remember, we expressed this idea of 'adding 2 to every function output' very clearly using algebra. We let $y=f(x)$ be the function values, and then used the expression $f(x) + 2$ to translate every function value up by 2 units.

In general, we can write the vertical translation of a function $f(x)$ by $v$ units by the expression

$$ 
f(x) + v. 
$$

WAIT A MINUTE!! This notation makes it seem like we can only translate functions **up**! We need to keep in mind that if we wanted to translate a function **down**, then we would select a **negative** value for $v$. The translations resulting from values of $v$ are shown in the this table: 

Value of $v$ | Effect on graph of function
:-- | :--
Positive | Translates **up**
Negative | Translates **down**


You can play with different values of $v$ in the widget that comes after the next section.

## Horizontal Translations

Now you're getting used to vertical translations, so let's move to the next concept: moving a function from side to side. We'll use the same function from the last section, $f(x) = x$.

Suppose we add 2 to every function input value. In other words, before we put an $x$ value into our function, we add 2 to it. The table of function inputs and outputs now looks like this:

$$
\begin{array}{c|c}
x + 2 & y=f(x) \\ \hline
-2+2 = 0 & -2 \\
-1+2 = 1 & -1 \\ 
0+2 = 2 & 0 \\
1+2 = 3 & 1 \\
2+2 = 4 & 2
\end{array}
$$

Now let's plot the result of shifting the function inputs. It's ok to be uneasy about the $y$-values in the above table. We'll explain that right after we look at the graph of the translated function.

x = np.linspace(-10,10,200)
y1 = x
y2 = x+2

g1 = go.Scatter(
    x = x,
    y = y1,
    name = 'Original function')
g2 = go.Scatter(
    x = x,
    y = y2,
    name = 'Translated function')

fig = go.Figure([g1,g2])
fig.update_layout(title='Plot of two diagonal lines: y = x and y = (x+2)',
                   xaxis_title='x values',
                   yaxis_title='y values')
fig.show()

This plot shows something unexpected. When we added 2 to the $x$ values, the whole graph of the function moved to the *left*. Maybe you expected the graph of the function to move to the right. 

Let's keep in mind what actually happened when we added 2 to the $x$ values. By adding 2 units to $x=1$, for example, we essentially told the function to take on the output value it would normally take on at $x=3$, but instead when $x=1$.

In general, we can express any horizontal translation by $h$ units using the algebraic expression:

$$ 
f(x-h). 
$$

The effects of different values of $h$ are given in this table:

Value of $h$ | Effect on graph of function
:-- | :--
Positive | Translates **left**
Negative | Translates **right**

### Combining Vertical and Horizontal Translations

Now it's time for you to play with different vertical and horizontal translations. The widget below lets you set values for $v$ and $h$, and you will see how the displayed equation of the function changes. We'll use the function $y = \arctan(x-h) + v$.

# Hide this.

x = np.linspace(-10,10,200)

fig = go.Figure(go.Scatter(x=x,y=x**2))
fig.update_layout(title='y=arctan(x-(0.0)) + (0.0)',
                   xaxis_title='x values', xaxis_range=[-5,5],xaxis_zeroline=True,
                   yaxis_title='y values', yaxis_range=[-5,5],yaxis_zeroline=True)

def View1(h, v):
    fig.update_layout(title='y = arctan(x -(' + str(h) + ')) + (' + str(v) + ')',
                   xaxis_title='x values', xaxis_range=[-5,5],xaxis_zeroline=True,
                   yaxis_title='y values', yaxis_range=[-5,5],yaxis_zeroline=True)
    x = np.linspace(-10,10,200)
    fig.update_traces(x=x,y = np.arctan(x - h) + v)
    fig.show()

import warnings
import sys
if not sys.warnoptions:
    warnings.simplefilter("ignore")

interactive_plot = widgets.interactive(View1, 
                               v = (-5,5,0.5), 
                               h = (-5,5,0.5),
                               continuous_update=True,
                               wait=True)

output = interactive_plot.children[-1]
output.layout.height = '600px'
output.layout.width = '600px'
output.clear_output(wait=True) 
interactive_plot

### *Exercise*
The graph is an arc with its highest point at the coordinate pair $(x,y)=(2,0)$. Move the graph so that the top of the arc is at $(2,-3)$, $(-4,6)$, $(10,0)$, and $(0,10)$. What are the values of $v$ and $h$ at each of these places?

# Hide this.

def func(x, v, h):
    return np.abs(np.sqrt(4-(x-2+h)**2)) - 2 + v

x1 = np.linspace(-10,10,200)
fig = go.Figure(go.Scatter(x=x1,y=func(x1,0.0,0.0)))
fig.update_layout(title='y = y = f(x-h) + v, an arc',
                   xaxis_title='x values', xaxis_range=[-10,10],xaxis_zeroline=True,
                   yaxis_title='y values', yaxis_range=[-10,10],yaxis_zeroline=True)
fig.update_xaxes(tick0=2.0, dtick=2.0)
fig.update_yaxes(tick0=2.0, dtick=2.0)

def View(v, h):
    x1 = np.linspace(-10,10,200)
    fig.update_traces(x=x1,y = func(x1, v, h))
    fig.update_layout(title='y = f(x-h) + v, an arc')
    fig.show()

import warnings
import sys
if not sys.warnoptions:
    warnings.simplefilter("ignore")

interactive_plot = widgets.interactive(View, 
                               v = (-10,10,1), 
                               h = (-10,10,1),
                               continuous_update=True,
                               wait=True)

output = interactive_plot.children[-1]
output.layout.height = '600px'
output.layout.width = '600px'
output.clear_output(wait=True) 
interactive_plot

### *Exercises*

1.  Write the expression for translating the function $f(x) = \sqrt{x}$ **down** by 4 units and **right** by 3 units. 
2.  The graph of the function $f(x) = x^2 - 2x - 3 = (x+1)(x-3)$ touches the $x$-axis at the two points $x=-1$ and $x=3$. What vertical translation can be applied to this function so that it only touches the $x$-axis when $x=1$? 
3.  What happens to the graph of a constant function $f(x)=c$ when the function is translated horizontally? Vertically? </li>
4.  Write a Python function that allows the user to specify input values 'x', an output function to be translated 'f', and the vertical and horizontal translation parameters $k$ and $h$. Your function should have four inputs: x, f, $h$, and $k$. A template is provided in the next cell. Show that your function works on the function 'testf'. 


%%html
<button onclick="javascript:code_toggle()">CLICK HERE TO SHOW THE CODE CELL FOR THIS EXERCISE.</button> 

# Write your translation function from Exercise 4 here.

def translate(x, f, v, h):
    return f(x)   # put your formula here
    
    pass

# A test function
def testf(x):
    return np.exp(-x**2)*0.4



# Test your translation function here.
h = 1     # Replace with a value of h
v = 0     # Replace with a value of v

x = np.linspace(-10,10,200)
y = translate(x, testf, v, h)


# Uncomment these lines to plot the translated function (select the lines and press 'CTRL  /').
#fig = go.Figure([go.Scatter(x=x,y=y,name='Translated'),go.Scatter(x=x,y=testf(x),name='Original')])
#fig.show()



### *Exercise*

In the maze below, use horizontal and vertical translations to move the dot from its current position to the red circle. There are lots of ways to get there, but try to find the fastest possible route. Don't travel through any buildings!

# Hide this.

# These are the coordinates for each 'building' rectangle. They are in the form
# x0, x1, y0, y1.
b_coords = [[-9.8,-6.2,-7.8,-6.2], [-9.8,-1.2,-9.8,-9.2], [-4.8,-0.2,-7.8,-0.2],
            [-8.8,-1.2,0.2,3.8], [-8.8,-6.2,-4.8,-1.2], [0.2,8.8,-8.8,-8.2],
            [1.2,9.8,-6.8,-1.2], [0.2,7.8,0.2,4.8], [9.2,9.8,0.2,9.8],
            [9.2,9.8,0.2,9.8], [0.2,7.8,6.2,8.8], [-3.8,-1.2,5.2,7.8],
            [-9.8,-5.2,5.2,9.8], [-3.8,-1.2,9.2,9.8]]

def View(v, h):   
    trace = go.Scatter(x=[0],y=[0],mode='markers')
    
    layout = {
    'xaxis': {
        'range': [-10, 10],
        'zeroline': True
    },
    'yaxis': {
        'range': [-10, 10],
        'zeroline': True
    },
    'shapes': [
        # filled circle
        {
            'type': 'circle',
            'xref': 'x',
            'yref': 'y',
            'fillcolor': 'rgba(50, 171, 96, 0.7)',
            'x0': -9+h,
            'y0': -9+v,
            'x1': -8+h,
            'y1': -8+v,
            'line': {'color': 'rgba(50, 171, 96, 1)'}
        },
        # end point
        {
            'type': 'circle',
            'xref': 'x',
            'yref': 'y',
            'fillcolor': 'rgba(255, 0, 0, 0.7)',
            'x0': -1,
            'y0': 8,
            'x1': 0,
            'y1': 9,
            'line': {'color': 'rgba(255, 0, 0, 1)'}
        }
    ]
    }
    # Add the 'building' obstacles.
    for i in range(len(b_coords)):
        building = {'type':'rect','xref':'x','yref':'y',
                    'fillcolor':'rgba(102, 51, 0, 0.7)','line':{'color':'rgba(102, 51, 0, 1)'},
                            'x0':b_coords[i][0],'x1':b_coords[i][1],'y0':b_coords[i][2],'y1':b_coords[i][3]}
        layout['shapes'].append(building)
        
    fig = go.Figure(data=[trace],layout=layout)
    fig.update_layout(title='Using the sliders, move the green circle to the red one.')
    fig.show()

import warnings
import sys
if not sys.warnoptions:
    warnings.simplefilter("ignore")

interactive_plot = widgets.interactive(View, 
                               v = (-20,20,1), 
                               h = (-20,20,1),
                               continuous_update=True,
                               wait=True)

output = interactive_plot.children[-1]
output.layout.height = '600px'
output.layout.width = '600px'
output.clear_output(wait=True) 
interactive_plot

## What have we learned?

Translating a function just takes adding or subtracting number to the function definition.

The function $y=f(x)$ is moved up by two units when we change it to $y=f(x)+2$.

The function $y=f(x)$ is moved to the right by two units when we change it to $y=f(x-2)$.

Notice for vertical moves, the number 2 is added **outside** the function. For horizontal moves, the number 2 is subtracted **inside** the function, next to the variable $x$.

[![Callysto.ca License](https://github.com/callysto/curriculum-notebooks/blob/master/callysto-notebook-banner-bottom.jpg?raw=true)](https://github.com/callysto/curriculum-notebooks/blob/master/LICENSE.md)