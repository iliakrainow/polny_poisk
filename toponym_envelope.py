def get_toponym_envelope(toponym):
    toponym_coodrinates = toponym["Point"]["pos"]
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
    ll = ','.join([toponym_longitude, toponym_lattitude])
    envelope = toponym['boundedBy']['Envelope']

    l, b = envelope['lowerCorner'].split()
    r, t = envelope['upperCorner'].split()

    dx = abs(float(l) - float(r)) / 2
    dy = abs(float(t) - float(b)) / 2

    span = f"{dx},{dy}"
    return (ll, span)
