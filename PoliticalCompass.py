from pylab import *
import matplotlib.pyplot as plt
import numpy
import numbers
flag = 1


end = 0
x_prime = 9.99649
y_prime = -16.4683


x = [10,10,10,10]
y = [0,15,0,-15]


start = input('Welcome to my political compass, you will be given various statements, type "Y" if you agree with them'
              ' and "N" if you do not. If nuetral, type "b". Press k to start')
if start == 'k':
    x_prime = 9.99649
    y_prime = -16.4683

elif start != 'k':
    while flag == 1:
        start = input(
        'Welcome to my political compass, you will be given various statements, type "Y" if you agree with them'
        ' and "N" if you do not. Press k to start')

question_one = input('1: A flat tax system where everybody pays the same rate regardless of'
                     ' income is preferable to a progressive tax system that taxes the rich at a higher rate.')
if question_one == 'Y' or question_one == 'y':
    x_prime += 0.0000701
elif question_one == 'B' or question_one == 'b':
    x_prime += 0.00003505

question_two = input("2: A private health care system where individuals purhcase medical treatment on their own is preferable to a government run health insurance plan.")

if question_two == 'Y' or question_two == 'y':
    x_prime += 0.0000701
elif question_two == 'b' or question_two == 'B':
    x_prime += 0.0003505

question_three = input('3: Businesses should be able to fire workers for attempting to organize labor unions: ')

if question_three == 'Y' or question_three == 'y':
    x_prime += 0.0000701
elif question_three == 'b' or question_three == 'B':
    x_prime += 0.0003505

question_four = input('4: Barriers to international free trade in goods and services should be reduced and/or eliminated: ')

if question_four == 'Y' or question_four == 'y':
    x_prime += 0.0000701
elif question_four == 'b' or question_four == 'B':
    x_prime += 0.0003505

question_five = input('5: The government should not do anything to help students afford tuition for higher education: ')

if question_five == 'Y' or question_five == 'y':
    x_prime += 0.0000701
elif question_five == 'b' or question_five == 'B':
    x_prime += 0.0003505

question_six = input('6: Government budgets should always be balanced regardless of which programs have to be cut.')

if question_six == 'Y' or question_six == 'y':
    x_prime += 0.0000701
elif question_six == 'b' or question_six == 'B':
    x_prime += 0.0003505

question_seven = input('7: The government has no responsibility to provide a social'
                       ' safety net; helping the poor should be left up to private charities and individuals: ')

if question_seven == 'Y' or question_seven == 'y':
    x_prime += 0.0000701
elif question_seven == 'b' or question_seven == 'B':
    x_prime += 0.0003505

question_eight = input('8: Social security and state pension funds should be privatized: ')

if question_eight == 'Y' or question_eight == 'y':
    x_prime += 0.0000701
elif question_eight == 'b' or question_eight == 'B':
    x_prime += 0.0003505

question_nine = input('9: Things like arts and humanities should be funded solely by private organizations and never via public funds: ')

if question_nine == 'Y' or question_nine == 'y':
    x_prime += 0.0000701
elif question_nine == 'b' or question_nine == 'B':
    x_prime += 0.0003505

question_ten = input('10: Man made global warming is a myth and nothing should be done to limit the amount of CO2 emissions because doing so will only harm the economy.')

if question_ten == 'Y' or question_ten == 'y':
    x_prime += 0.0000701
elif question_ten == 'b' or question_ten == 'B':
    x_prime += 0.0003505


question_eleven = input('11: Pregnant women should not have unlimited access to abortion, it ought to be illegal in some or all cases.')

if question_eleven == 'Y' or question_eleven == 'y':
    y_prime += 3.29464
elif question_eleven == 'b' or question_eleven == 'B':
    y_prime += 1.64732

question_twelve = input('12: Censorship of the media is sometimes necessary to protect public morality: ')
if question_twelve == 'Y' or question_twelve == 'y':
    y_prime += 3.29464
elif question_twelve == 'b' or question_twelve == 'B':
    y_prime += 1.64732

question_thirteen = input('13: Marriage between parties other than monogamous heterosexual couples (i.e. one man, one woman) should be prohibited: ')
if question_thirteen == 'Y' or question_thirteen == 'y':
    y_prime += 3.29464
elif question_thirteen == 'b' or question_thirteen == 'B':
    y_prime += 1.64732

question_fourteen = input('14: Users of recreational drugs like marijuana should be subject to criminal prosecution: ')
if question_fourteen == 'Y' or question_fourteen == 'y':
    y_prime += 3.29464
elif question_fourteen == 'b' or question_fourteen == 'B':
    y_prime += 1.64732

question_fifteen = input('15: It should be legal to torture suspected terrorists and enemy combatants in order to get information: ')
if question_fifteen == 'Y' or question_fifteen == 'y':
    y_prime += 3.29464
elif question_fifteen == 'b' or question_fifteen == 'B':
    y_prime += 1.64732

question_sixteen = input('16: Every young adult should be subject to a term of mandatory military or community service: ')
if question_sixteen == 'Y' or question_sixteen == 'y':
    y_prime += 3.29464
elif question_sixteen == 'b' or question_sixteen == 'B':
    y_prime += 1.64732

question_seventeen = input('17: There should be a biometrically enhanced national ID card which citizens should be required to carry at all times: ')
if question_seventeen == 'Y' or question_seventeen == 'y':
    y_prime += 3.29464
elif question_seventeen == 'b' or question_seventeen == 'B':
    y_prime += 1.64732

question_eighteen = input('18: Strict immigration restrictions should be put in place in order to prevent the erosion of our nation’s culture and way of life by large numbers of newcomers: ')
if question_eighteen == 'Y' or question_eighteen == 'y':
    y_prime += 3.29464
elif question_eighteen == 'b' or question_eighteen == 'B':
    y_prime += 1.64732

question_nineteen = input('19: Individuals whose political viewpoints threaten the legitimacy of the regime should be prohibited from taking part in the political process; ')
if question_nineteen == 'Y' or question_nineteen == 'y':
    y_prime += 3.29464
elif question_nineteen == 'b' or question_nineteen == 'B':
    y_prime += 1.64732

question_twenty = input('20: Preemptive military action against enemy countries is at times necessary to stop threats before they start, even if the United Nations and international community is in opposition: '
                        )
if question_twenty == 'Y' or question_twenty == 'y':
    y_prime += 3.29464
    end = 10
elif question_twenty == 'b' or question_twenty == 'B':
    y_prime += 1.64732
    end = 10
else:
    end = 10

color = ['m','g','r','b']


fig = plt.figure()
ax = fig.add_subplot(111)

scatter(x,y, s=10 ,marker='o', c=color)

left,right = ax.get_xlim()
low,high = ax.get_ylim()


import matplotlib.lines as mlines

def newline(p1, p2):
    ax = plt.gca()
    xmin, xmax = ax.get_xbound()

    if(p2[0] == p1[0]):
            xmin = xmax = p1[0]
            ymin, ymax = ax.get_ybound()
    else:
            ymax = p1[1]+(p2[1]-p1[1])/(p2[0]-p1[0])*(xmax-p1[0])
            ymin = p1[1]+(p2[1]-p1[1])/(p2[0]-p1[0])*(xmin-p1[0])

    l = mlines.Line2D([xmin,xmax], [ymin,ymax])
    ax.add_line(l)
    return l


plt.xlabel('Libertarian')
plt.ylabel('Left')
plt.title('Authoritarian')
ax.yaxis.tick_right()
ax2 = ax.twinx()
ax2.set_ylabel('Right')

arrow( left, 0, right -left, 0, length_includes_head = True, head_width = 0.15 )
arrow( 0, low, 0, high-low, length_includes_head = True, head_width = 0.15 )

plt.plot(x, y)

if end == 10:

    if x_prime < 9.99650:
        plt.scatter(9.9965, y_prime)
    if 9.9970 > x_prime > 9.9965:
        plt.scatter(9.9970, y_prime)
    if 9.9970 < x_prime < 9.9975:
        plt.scatter(9.9975, y_prime)
    if 9.9975 < x_prime < 9.998:
        plt.scatter(9.998, y_prime)
    if 9.998 < x_prime < 9.9985:
        plt.scatter(9.9985, y_prime)
    if 9.9985 < x_prime < 9.9990:
        plt.scatter(9.9990, y_prime)
    if 9.999 < x_prime < 9.9995:
        plt.scatter(9.995, y_prime)

    if 9.9995 < x_prime < 10:
        plt.scatter(10, y_prime)
    if 10 < x_prime < 10.00050:
        plt.scatter(10.005, y_prime)
    if 10.0005 < x_prime < 10.0010:
        plt.scatter(10.001, y_prime)
    if 10.0010 < x_prime < 10.0015:
        plt.scatter(10.0015, y_prime)
    if 10.0015 < x_prime < 10.0020:
        plt.scatter(10.002, y_prime)
    if 10.002 < x_prime < 10.0025:
        plt.scatter(10.0025, y_prime)
    if 10.0025 < x_prime < 10.0030:
        plt.scatter(10.003, y_prime)
    if 10.003 < x_prime < 10.0035:
        plt.scatter(10.0035, y_prime)

print(x_prime)
print(y_prime)
plt.show()
