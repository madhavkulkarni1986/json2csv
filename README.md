### Examples:

**$ python json2csv.py example.json test.csv**

**$ cat example.json**

[
        {
                "Name": "Debian",
                "Version": "9",
                "Install": "apt",
                "Owner": "SPI",
                "Kernel": "4.9"
        },
        {
                "Name": "Ubuntu",
                "Version": "17.10",
                "Install": "apt",
                "Owner": "Canonical",
                "Kernel": "4.13"
        },
        {
                "Name": "Fedora",
                "Version": "26",
                "Install": "dnf",
                "Owner": "Red Hat",
                "Kernel": "4.13"
        },
        {
                "Name": "CentOS",
                "Version": "7",
                "Install": "yum",
                "Owner": "Red Hat",
                "Kernel": "3.10"
        },
        {
                "Name": "OpenSUSE",
                "Version": "42.3",
                "Install": "zypper",
                "Owner": "Novell",
                "Kernel": "4.4"
        },
        {
                "Name": "Arch Linux",
                "Version": "Rolling Release",
                "Install": "pacman",
                "Owner": "SPI",
                "Kernel": "4.13"
        },
        {
                "Name": "Gentoo",
                "Version": "Rolling Release",
                "Install": "emerge",
                "Owner": "Gentoo Foundation",
                "Kernel": "4.12"
        }
]

**$ cat test.csv**

Name,Version,Install,Owner,Kernel
Debian,9,apt,SPI,4.9
Ubuntu,17.10,apt,Canonical,4.13
Fedora,26,dnf,Red Hat,4.13
CentOS,7,yum,Red Hat,3.10
OpenSUSE,42.3,zypper,Novell,4.4
Arch Linux,Rolling Release,pacman,SPI,4.13
Gentoo,Rolling Release,emerge,Gentoo Foundation,4.12

**$ python json2csv.py wrong_file.json test.csv**

JSON file error => Extra data: line 8 column 3 (char 100)

**$ cat wrong_file.json**

        {
                "Name": "Debian",
                "Version": "9",
                "Install": "apt",
                "Owner": "SPI",
                "Kernel": "4.9"
        },
        {
                "Name": "Ubuntu",
                "Version": "17.10",
                "Install": "apt",
                "Owner": "Canonical",
                "Kernel": "4.13"
        },
        {
                "Name": "Fedora",
                "Version": "26",
                "Install": "dnf",
                "Owner": "Red Hat",
                "Kernel": "4.13"
        },
        {
                "Name": "CentOS",
                "Version": "7",
                "Install": "yum",
                "Owner": "Red Hat",
                "Kernel": "3.10"
        },
        {
                "Name": "OpenSUSE",
                "Version": "42.3",
                "Install": "zypper",
                "Owner": "Novell",
                "Kernel": "4.4"
        },
        {
                "Name": "Arch Linux",
                "Version": "Rolling Release",
                "Install": "pacman",
                "Owner": "SPI",
                "Kernel": "4.13"
        },
        {
                "Name": "Gentoo",
                "Version": "Rolling Release",
                "Install": "emerge",
                "Owner": "Gentoo Foundation",
                "Kernel": "4.12"
        }

