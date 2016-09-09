#ME701_Rajarshi_Fall16_HW2_Problem1

# Temperature conversion from Fahrenheit to Degree Celsius

echo -n "Enter temperature in Fahrenheit Scale: "

read F


echo "The temperature in Fahrenheit scale is F=$F"

C=$(echo "((5/9)*($F-32))" | bc -l)

echo "The temperature in Celsius scale is C=$C"











