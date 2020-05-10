import sys
import re


def modify_java_security_file(rfp, wfp):
    with open(fp, 'r') as file:
        lines = file.readlines()

    regex1 = r"^jdk\.certpath\.disabledAlgorithms=(.*)\\$"
    regex2 = r"^jdk\.tls\.disabledAlgorithms=(.*)\\$"
    regex3 = r"^jdk\.jar\.disabledAlgorithms=(.*)$"
    re.compile(regex1)
    re.compile(regex2)
    re.compile(regex3)
    changed = []
    #print(len(lines))

    for i in range(len(lines)):
        match1 = re.search(regex1, lines[i])
        match2 = re.search(regex2, lines[i])
        match3 = re.search(regex3, lines[i])
        if match1:
            str1 = match1.group(0)
            print(match1.group(0))
            if "\\" in str1:
                lines[i] = "#" + lines[i]
                lines[i + 1] = "#" + lines[i + 1]
                changed.append(lines[i])
                changed.append(lines[i + 1])
            else:
                lines[i] = "#" + lines[i]
                changed.append(lines[i])

        elif match2:
            str2 = match2.group(0)
            print(match2.group(0))
            if "\\" in str2:
                lines[i] = "#" + lines[i]
                lines[i + 1] = "#" + lines[i + 1]
                changed.append(lines[i])
                changed.append(lines[i + 1])
            else:
                lines[i] = "#" + lines[i]
                changed.append(lines[i])
        elif match3:
            print(match3.group(0))
            str3 = match3.group(0)
            if "\\" in str3:
                lines[i] = "#" + lines[i]
                lines[i + 1] = "#" + lines[i + 1]
                changed.append(lines[i])
                changed.append(lines[i + 1])
            else:
                lines[i] = "#" + lines[i]
                changed.append(lines[i])

        else:
            continue

    new_params = ["jdk.certpath.disabledAlgorithms=MD2", "jdk.tls.disabledAlgorithms=SSLv3, RC4, DES, K_NULL, C_NULL, M_NULL, DH_anon, ECDH_anon, DH keySize < 1024, RSA keySize < 256, EC keySize < 224",
                  "jdk.jar.disabledAlgorithms=MD2, MD5, RSA keySize < 256"]
    lines = lines + new_params
    print(changed)
    print(len(changed))

    with open(wfp, 'w') as wf:
        for line in lines:
            wf.write("%s\n" % line.strip())


if __name__ == "__main__":
    fp = sys.argv[1]
    #print(fp)
    wfp = "new_file"
    modify_java_security_file(fp, wfp)
