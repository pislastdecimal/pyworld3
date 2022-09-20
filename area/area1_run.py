import pyworld3
from pyworld3 import World3
from pyworld3.utils import plot_world_variables
from matplotlib.pyplot import rcParams, show

"""AREAs"""
import area.area1_constants as a1

params = {'lines.linewidth': '3'}
rcParams.update(params)

area1_json = "./area1_functions_table.json"

def run():
    area1 = World3(verbose=True)  # choose the time limits and step.
    # area1.init_world3_constants()
    area1.init_world3_constants(p1i=a1.p1i, p2i=a1.p2i, p3i=a1.p3i, p4i=a1.p4i,
                                dcfsn=a1.dcfsn, fcest=a1.fcest, hsid=a1.hsid, ieat=a1.ieat, len=a1.len,
                                lpd=a1.lpd, mtfn=a1.mtfn, pet=a1.pet, rlt=a1.rlt, sad=a1.sad,
                                zpgt=a1.zpgt, ici=a1.ici, sci=a1.sci, iet=a1.iet, iopcd=a1.iopcd,
                                lfpf=a1.lfpf, lufdt=a1.lufdt, icor1=a1.icor1, icor2=a1.icor2, scor1=a1.scor1,
                                scor2=a1.scor2, alic1=a1.alic1, alic2=a1.alic2, alsc1=a1.alsc1, alsc2=a1.alsc2,
                                fioac1=a1.fioac1, fioac2=a1.fioac2,
                                ali=a1.ali, pali=a1.pali, lfh=a1.lfh, palt=a1.palt,
                                pl=a1.pl, alai1=a1.alai1, alai2=a1.alai2, io70=a1.io70, lyf1=a1.lyf1,
                                lyf2=a1.lyf2, sd=a1.sd, uili=a1.uili, alln=a1.alln, uildt=a1.uildt,
                                lferti=a1.lferti, ilf=a1.ilf, fspd=a1.fspd, sfpc=a1.sfpc,
                                ppoli=a1.ppoli, ppol70=a1.ppol70, ahl70=a1.ahl70, amti=a1.amti,
                                imti=a1.imti, imef=a1.imef, fipm=a1.fipm, frpm=a1.frpm,
                                ppgf1=a1.ppgf1, ppgf2=a1.ppgf2, ppgf21=a1.ppgf21, pptd1=a1.pptd1, pptd2=a1.pptd2,
                                nri=a1.nri, nruf1=a1.nruf1, nruf2=a1.nruf2
                                )  # choose the model constants.
    area1.init_world3_variables()  # initialize all variables.
    area1.set_world3_table_functions(json_file=area1_json)  # get tables from a json file.
    area1.set_world3_delay_functions()  # initialize delay functions.
    area1.run_world3()

    plot_world_variables(area1.time,
                         [area1.nrfr, area1.iopc, area1.fpc,
                          area1.ppolx, area1.pop],
                         ["NRFR", "IOPC", "FPC", "PPOLX", "POP"],
                         [[0, 1], [0, 1e3], [0, 1e3], [0, 32], [0, 16e9]],
                         figsize=(7, 5),
                         grid=1,
                         title="World3 BRUNO run")

    show()
