import struct

def sid_to_str(sid):
    """
    Convert a binary or hex SID to string form 'S-1-5-21-...'
    Works with Python 3.12+.
    """
    # Accept either bytes or hex string
    if isinstance(sid, str):
        s = sid.strip().lower().replace("0x", "").replace("b'", "").replace("'", "")
        sid = bytes.fromhex(s)
    elif not isinstance(sid, (bytes, bytearray)):
        raise TypeError("sid must be bytes, bytearray, or hex string")

    if len(sid) < 8:
        raise ValueError("SID is too short")

    revision = sid[0]
    sub_id_count = sid[1]

    # Identifier Authority (6 bytes, big-endian, pad to 8 bytes for unpack)
    iav = struct.unpack(">Q", b"\x00\x00" + sid[2:8])[0]

    # Sub-authorities (4 bytes each, little-endian)
    sub_ids = [
        struct.unpack("<I", sid[8 + 4 * i:12 + 4 * i])[0]
        for i in range(sub_id_count)
    ]

    return f"S-{revision}-{iav}-" + "-".join(str(x) for x in sub_ids)

print(sid_to_str("0105000000000005150000005b7bb0f398aa2245ad4a1ca451040000"))