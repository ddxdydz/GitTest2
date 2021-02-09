def get_spn(toponym):
    lowerCorner, upperCorner = [v.split() for v in toponym[
        "boundedBy"]["Envelope"].values()]
    spn_delta_1 = float(upperCorner[0]) - float(lowerCorner[0])
    spn_delta_2 = float(upperCorner[1]) - float(lowerCorner[1])
    return str(spn_delta_1), str(spn_delta_2)
