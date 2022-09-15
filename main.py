from hapaglloydhandle import HapagLloydHandle

if __name__ == '__main__':

    bls = [
        'HLCUME3220853551', 'HLCUME3220855725', 'HLCUBSC2208BGAZ4', 'HLCUBSC220844170', 'HLCUSHA2112NDAV4',
        'HLCUBSC220857080', '0122018132', 'HLCUBSC2208BQQB9', 'HLCUME3220761733', 'HLCUTPE220785476',
        'HLCUME3220850319', 'HLCUME3220644774', 'HLCUME3220855546', 'HLCUME3220855831', 'HLCUBO2220841617',
        'HLCUME3220850184', '11112004396', '11112004395', '11112004397', 'BKK00018002', 'MTYSL2207OE2763',
        'HLCUDUR220840246', 'HLCUME3220850268', 'HLCUME3220855389', 'HLCUME3220855356', 'HLCUBSC2207AUCQ1',
        'HLCUBSC220855706', 'HLCUBSC220837256', '0122019046', '0122019040', 'HLCUME3220736168', 'HLCUBKK220817775',
        'HLCULGB220812833', '11112004394', '11112004290', 'HLCUBSC220800214', 'HLCUME3220850374', 'HLCUNG12205WTPD0',
        'CA1001055920', 'HLCUBSC2208BQXG7', 'HLCUTPE220762899', '6440045533', 'GLVSKR0031468', 'HLCUBSC2208BOGH9',
        'HLCUTA12208DFJUO', 'HLCUSHA2112NDDC7', 'HLCUME3220854174', 'HLCUGDY220568797', 'HLCUBO2220904808'
    ]

    hapaglloydhandle = HapagLloydHandle('files/')
    for bl in bls:
        hapaglloydhandle.handle(bl)
