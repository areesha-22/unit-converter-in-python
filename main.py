import streamlit as st

# Page title
st.header("UNIT CONVERTOR USING PYTHON")
st.write("Easily convert between different units of length, weight, and temperature.")

# Sidebar selection
conversion_type = st.sidebar.selectbox("Choose conversion type", ["length", "weight", "temperature"])

# User input value
value = st.number_input("Enter value", value=0.0, min_value=0.0, step=0.1)

col1, col2 = st.columns(2)

# Unit selection
if conversion_type == "length":
    with col1:
        from_unit = st.selectbox("From", ["Meter", "kilometer", "centimeter", "milimeter", "nanometer", "miles", "yards"])
    with col2:
        to_unit = st.selectbox("To", ["Meter", "kilometer", "centimeter", "milimeter", "miles", "yards"])

elif conversion_type == "weight":
    with col1:
        from_unit = st.selectbox("From", ["gram", "kilogram", "miligram", "pounds", "ounces"])
    with col2:
        to_unit = st.selectbox("To", ["gram", "kilogram", "miligram", "pounds", "ounces"])

elif conversion_type == "temperature":
    with col1:
        from_unit = st.selectbox("From", ["celsius", "fahrenheit", "kelvin"])
    with col2:
        to_unit = st.selectbox("To", ["celsius", "fahrenheit", "kelvin"])

# Conversion functions
def length_converter(value, from_unit, to_unit):
    length_units = {
        'Meter': 1, 'kilometer': 0.001, 'centimeter': 100, 'milimeter': 1000,
        'miles': 0.000621371, 'yards': 1.09361, 'feet': 3.28084, 'inches': 39.3701
    }
    return (value / length_units[from_unit]) * length_units[to_unit]

def weight_converter(value, from_unit, to_unit):
    weight_units = {
        'kilogram': 1, 'gram': 1000, 'miligram': 1000000, 'pounds': 2.20462,
        'ounces': 35.274
    }
    return (value / weight_units[from_unit]) * weight_units[to_unit]

def temperature_converter(value, from_unit, to_unit):
    if from_unit == "celsius":
        if to_unit == "fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "kelvin":
            return value + 273.15
        else:
            return value  # If same unit

    elif from_unit == "fahrenheit":
        if to_unit == "celsius":
            return (value - 32) * 5/9
        elif to_unit == "kelvin":
            return (value - 32) * 5/9 + 273.15
        else:
            return value

    elif from_unit == "kelvin":
        if to_unit == "celsius":
            return value - 273.15
        elif to_unit == "fahrenheit":
            return (value - 273.15) * 9/5 + 32
        else:
            return value

    else:
        return "Invalid unit"

# Initialize result
result = None

# Convert Button
if st.button("CONVERT"):
    if conversion_type == "length":
        result = length_converter(value, from_unit, to_unit)
    elif conversion_type == "weight":
        result = weight_converter(value, from_unit, to_unit)
    elif conversion_type == "temperature":
        result = temperature_converter(value, from_unit, to_unit)

# Display result if available
if result is not None:
    st.markdown(f"**{value} {from_unit} = {result:.4f} {to_unit}**")
st.write("created by AREESHA")