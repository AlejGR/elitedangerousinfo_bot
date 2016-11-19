#encoding=utf8
from config import *

@bot.message_handler(func=lambda m: m.content_type == 'text' and m.text in ['Productos'])
@bot.message_handler(commands=['productos'])
def command_productos(m):
    cid = m.chat.id
    bot.send_message(cid,"introduzca el nombre del producto")
    name = m.text
    userStep[m.from_user.first_name] = 'productos'

@bot.message_handler(func=lambda m: get_user_step(m.from_user.first_name) == 'productos', content_types=['text'])
def productosstep(m):
    if len(m.text) >= 1:
        cid = m.chat.id
        name = m.text[:20]
        userStep[m.from_user.first_name] = 0
        ##################
        #   TRADUCCIÓN   #
        ##################
        if name.lower() == 'explosivos':
            name = 'Explosives'
        elif name.lower() == 'combustible de hidrógeno':
            name = 'Hydrogen Fuel'
        elif name.lower() == 'combustible de hidrogeno':
            name = 'Hydrogen Fuel'
        elif name.lower() == 'peróxido de hidrógeno':
            name = 'Hydrogen Peroxide'
        elif name.lower() == 'peróxido de hidrogeno':
            name = 'Hydrogen Peroxide'
        elif name.lower() == 'oxígeno líquido':
            name = 'Liquid Oxygen'
        elif name.lower() == 'oxigeno liquido':
            name = 'Liquid Oxygen'
        elif name.lower() == 'aceite mineral':
            name = 'Mineral Oil'
        elif name.lower() == 'agentes nerviosos':
            name = 'Nerve Agents'
        elif name.lower() == 'pesticida':
            name = 'Pesticides'
        elif name.lower() =='estabilizadores de superficie':
            name = 'Surface Stabilisers'
        elif name.lower() == 'agentes sintéticos':
            name = 'Synthetic Reagents'
        elif name.lower() == 'agentes sinteticos':
            name = 'Synthetic Reagents'
        elif name.lower() == 'agua':
            name = 'Water'
        elif name.lower() == 'ropa':
            name = 'Clothing'
        elif name.lower() == 'tecnología de consumo':
            name = 'Consumer Technology'
        elif name.lower() == 'tecnologia de consumo':
            name = 'Consumer Technology'
        elif name.lower() == 'electrodomésticos':
            name = 'Domestic Appliances'
        elif name.lower() == 'refugio de evacuación':
            name = 'Evacuation Shelter'
        elif name.lower() == 'equipamiento de supervivencia':
            name = 'Survival Equipment'
        elif name.lower() == 'algas':
            name = 'Algae'
        elif name.lower() == 'carne de animales':
            name = 'Animal Meat'
        elif name.lower() == 'café':
            name = 'Coffee'
        elif name.lower() == 'cafe':
            name = 'Coffee'
        elif name.lower() == 'pescado':
            name = 'Fish'
        elif name.lower() == 'cartuchos de alimentos':
            name = 'Food Cartridges'
        elif name.lower() == 'frutas y verduras':
            name = 'Fruit and Vegetables'
        elif name.lower() == 'grano':
            name = 'Grain'
        elif name.lower() == 'carne sintética':
            name = 'Synthetic Meat'
        elif name.lower() == 'carne sintetica':
            name = 'Synthetic Meat'
        elif name.lower() == 'té':
            name = 'Tea'
        elif name.lower() == 'te':
            name = 'Tea'
        elif name.lower() == 'compuestos de cerámica':
            name = 'Ceramic Composites'
        elif name.lower() == 'compuestos de ceramica':
            name = 'Ceramic Composites'
        elif name.lower() == '':
            name = 'CMM Composite'
        elif name.lower() == '':
            name = 'Cooling Hoses'
        elif name.lower() == 'membrana de aislamiento':
            name = 'Insulating Membrane'
        elif name.lower() == 'meta-aleciones':
            name = 'Meta-Alloys'
        elif name.lower() == 'meta aleciones':
            name = 'Meta-Alloys'
        elif name.lower() == '':
            name = 'Neofabric Insulation'
        elif name.lower() == 'polímeros':
            name = 'Polymers'
        elif name.lower() == 'polimeros':
            name = 'Polymers'
        elif name.lower() == 'semiconductores':
            name = 'Semiconductors'
        elif name.lower() == 'superconductores':
            name = 'Superconductors'
        elif name.lower() == 'cerveza':
            name = 'Beer'
        elif name.lower() == 'licor de contrabando':
            name = 'Bootleg Liquor'
        elif name.lower() == 'licores':
            name = 'Liquor'
        elif name.lower() == 'narcóticos':
            name = 'Narcotics'
        elif name.lower() == 'narcoticos':
            name = 'Narcotics'
        elif name.lower() == 'tabaco':
            name = 'Tobacco'
        elif name.lower() == 'vino':
            name = 'Wine'
        elif name.lower() == 'motores articulados' :
            name = 'Articulation Motors'
        elif name.lower() == 'procesadores atmosféricos':
            name = 'Atmospheric Processors'
        elif name.lower() == 'procesadores atmosfericos':
            name = 'Atmospheric Processors'
        elif name.lower() == 'constructores':
            name = 'Building Fabricators'
        elif name.lower() == 'cosechadoras de cultivos':
            name = 'Crop Harvesters'
        elif name.lower() == 'células de energía de emergencia':
            name = 'Emergency Power Cells'
        elif name.lower() == 'celulas de energia de emergencia':
            name = 'Emergency Power Cells'
        elif name.lower() == 'celulas de energía de emergencia':
            name = 'Emergency Power Cells'
        elif name.lower() == 'colector de escape':
            name = 'Exhaust Manifold'
        elif name.lower() == 'equipamiento geológico':
            name = 'Geological Equipment'
        elif name.lower() == 'equipamiento geologico':
            name = 'Geological Equipment'
        elif name.lower() == '':
            name = 'Heatsink Interlink'
        elif name.lower() == '':
            name = 'HN Shock Mount'
        elif name.lower() == 'mineral de emisión magnética':
            name = 'Magnetic Emitter Coil'
        elif name.lower() == 'mineral de emision magnetica':
            name = 'Magnetic Emitter Coil'
        elif name.lower() == 'mineral de emisión magnetica':
            name = 'Magnetic Emitter Coil'
        elif name.lower() == 'equipamiento marino':
            name = 'Marine Equipment'
        elif name.lower() == 'hornos microbianos':
            name = 'Microbial Furnaces'
        elif name.lower() == 'extractor mineral':
            name = 'Mineral Extractors'
        elif name.lower() == 'terminales modulares':
            name = 'Modular Terminals'
        elif name.lower() == 'convertidor de energía':
            name = 'Power Converter'
        elif name.lower() == 'convertidor de energia':
            name = 'Power Converter'
        elif name.lower() == 'generadores de energía':
            name = 'Power Generators'
        elif name.lower() == 'generadores de energia':
            name = 'Power Generators'
        elif name.lower() == '':
            name = 'Power Grid Assembly'
        elif name.lower() == '':
            name = 'Power Transfer Conduits'
        elif name.lower() == '':
            name = 'Radiation Baffle'
        elif name.lower() == '':
            name = 'Reinforced Mounting Plate'
        elif name.lower() == '':
            name = 'Skimmer Components'
        elif name.lower() == 'unidades de refrigeramiento':
            name = 'Thermal Cooling Units'
        elif name.lower() == 'purificadores de agua':
            name = 'Water Purifiers'
        elif name.lower() == 'medicinas avanzadas':
            name = 'Advanced Medicines'
        elif name.lower() == 'medicinas agrícolas':
            name = 'Agri-Medicines'
        elif name.lower() == 'medicinas agricolas':
            name = 'Agri-Medicines'
        elif name.lower() == 'medicinas agricolas':
            name = 'Agri-Medicines'
        elif name.lower() == 'medicinas básicas':
            name = 'Basic Medicines'
        elif name.lower() == 'medicinas basicas':
            name = 'Basic Medicines'
        elif name.lower() == 'estabilizadores de combate':
            name = 'Combat Stabilisers'
        elif name.lower() == 'potenciadores de rendimiento':
            name = 'Performance Enhancers'
        elif name.lower() == 'células madre':
            name = 'Progenitor Cells'
        elif name.lower() == 'celulas madre':
            name = 'Progenitor Cells'
        elif name.lower() == 'aluminio':
            name = 'Aluminium'
        elif name.lower() == 'berilio':
            name = 'Beryllium'
        elif name.lower() == 'bismuto':
            name = 'Bismuth'
        elif name.lower() == 'cobalto':
            name = 'Cobalt'
        elif name.lower() == 'cobre':
            name = 'Copper'
        elif name.lower() == 'galio':
            name = 'Gallium'
        elif name.lower() == 'oro':
            name = 'Gold'
        elif name.lower() == 'hafnio 178':
            name = 'Hafnium 178'
        elif name.lower() == 'indio':
            name = 'Indium'
        elif name.lower() == 'lantano':
            name = 'Lanthanum'
        elif name.lower() == 'litio':
            name = 'Lithium'
        elif name.lower() == 'osmio':
            name = 'Osmium'
        elif name.lower() == 'paladio':
            name = 'Palladium'
        elif name.lower() == 'platino':
            name = 'Platinum'
        elif name.lower() == 'praseodimio':
            name = 'Praseodymium'
        elif name.lower() == 'samario':
            name = 'Samarium'
        elif name.lower() == 'plata':
            name = 'Silver'
        elif name.lower() == 'tantalio':
            name = 'Tantalum'
        elif name.lower() == 'talio':
            name = 'Thallium'
        elif name.lower() == 'torio':
            name = 'Thorium'
        elif name.lower() == 'titanio':
            name = 'Titanium'
        elif name.lower() == 'uranio':
            name = 'Uranium'
        elif name.lower() == 'bauxita':
            name = 'Bauxite'
        elif name.lower() == 'bertrandita':
            name = 'Bertrandite'
        elif name.lower() == 'bromellita':
            name = 'Bromellite'
        elif name.lower() == 'coltán':
            name = 'Coltan'
        elif name.lower() == 'coltan':
            name = 'Coltan'
        elif name.lower() == 'criolita':
            name = 'Cryolite'
        elif name.lower() == 'galita':
            name = 'Gallite'
        elif name.lower() == '':
            name = 'Goslarite'
        elif name.lower() == 'indita':
            name = 'Indite'
        elif name.lower() == 'jadeíta':
            name = 'Jadeite'
        elif name.lower() == 'jadeita':
            name = 'Jadeite'
        elif name.lower() == 'lepidolita':
            name = 'Lepidolite'
        elif name.lower() == 'hidróxido de litio':
            name = 'Lithium Hydroxide'
        elif name.lower() == 'hidroxido de litio':
            name = 'Lithium Hydroxide'
        elif name.lower() == 'diamante de baja temperatura':
            name = 'Low Temperature Diamond'
        elif name.lower() == 'hidrato de metano':
            name = 'Methane Clathrate'
        elif name.lower() == 'cristales de monohidrato de metanol':
            name = 'Methanol Monohydrate Crystals'
        elif name.lower() == 'moissanita':
            name = 'Moissanite'
        elif name.lower() == 'painita':
            name = 'Painite'
        elif name.lower() == 'pirofilita':
            name = 'Pyrophyllite'
        elif name.lower() == 'rutilo':
            name = 'Rutile'
        elif name.lower() == 'taaffeite':
            name = 'Taaffeite'
        elif name.lower() == 'uraninita':
            name = 'Uraninite'
        elif name.lower() == 'reliquias de Ai':
            name = 'Ai Relics'
        elif name.lower() == 'artefactos antiguos':
            name = 'Ancient Artefact'
        elif name.lower() == '':
            name = 'Antimatter Containment Unit'
        elif name.lower() == 'antibióticos':
            name = 'Antiquities'
        elif name.lower() == 'planes de asalto':
            name = 'Assault Plans'
        elif name.lower() == 'caja negra':
            name = 'Black Box'
        elif name.lower() == 'muestras comerciales':
            name = 'Commercial Samples'
        elif name.lower() == '':
            name = 'Data Core'
        elif name.lower() == 'papeles diplomáticos':
            name = 'Diplomatic Bag'
        elif name.lower() == 'correo encriptado':
            name = 'Encrypted Correspondence'
        elif name.lower() == 'almacenamiento de datos encriptados':
            name ='Encrypted Data Storage'
        elif name.lower() == 'químicos experimentales':
            name = 'Experimental Chemicals'
        elif name.lower() == '':
            name = 'Fossil Remnants'
        elif name.lower() == '':
            name = 'Galactic Travel Guide'
        elif name.lower() == 'muestras geológicas':
            name = 'Geological Samples'
        elif name.lower() == '':
            name = 'Hostage'
        elif name.lower() == 'inteligencia militar':
            name = 'Military Intelligence'
        elif name.lower() == 'planes militares':
            name = 'Military Plans'
        elif name.lower() == 'Idolos Misteriosos':
            name = 'Mysterious Idol'
        elif name.lower() == 'cápsula de criogenización ocupada':
            name = 'Occupied CryoPod'
        elif name.lower() == 'cápsula de escape ocupada':
            name = 'Occupied Escape Pod'
        elif name.lower() == 'efectos personales':
            name = 'Personal Effects'
        elif name.lower() == 'prisionero político':
            name = 'Political Prisoner'
        elif name.lower() == 'materiales de investigación prohibidos':
            name = 'Prohibited Research Materials'
        elif name.lower() == '':
            name = 'Prototype Tech'
        elif name.lower() == '':
            name = 'Rare Artwork'
        elif name.lower() == 'trasmisiones rebeldes':
            name = 'Rebel Transmissions'
        elif name.lower() == '':
            name = 'Salvageable Wreckage'
        elif name.lower() == '':
            name = 'Sap 8 Core Container'
        elif name.lower() == '':
            name = 'Scientific Research'
        elif name.lower() == 'muestras científicas':
            name = 'Scientific Samples'
        elif name.lower() == '':
            name = 'Space Pioneer Relics'
        elif name.lower() == 'datos tácticos':
            name = 'Tactical Data'
        elif name.lower() == '':
            name = 'Technical Blueprints'
        elif name.lower() == 'datos de comercio':
            name = 'Trade Data'
        elif name.lower() == 'artefactos desconocido':
            name = 'Unknown Artefact'
        elif name.lower() == '':
            name = 'Unstable Data Core'
        elif name.lower() == 'esclavos imperiales':
            name = 'Imperial Slaves'
        elif name.lower() == 'esclavos':
            name = 'Slaves'
        elif name.lower() == 'catalizadores avanzados':
            name = 'Advanced Catalysers'
        elif name.lower() == 'monitores animales':
            name = 'Animal Monitors'
        elif name.lower() == 'sistemas hidropónicos':
            name = 'Aquaponic Systems'
        elif name.lower() == '':
            name = 'Auto-Fabricators'
        elif name.lower() == '':
            name = 'Bioreducing Lichen'
        elif name.lower() == 'componentes de ordenadores':
            name = 'Computer Components'
        elif name.lower() == 'HE Suits':
            name = 'H.E. Suits'
        elif name.lower() == '':
            name = 'H.E. Suits'
        elif name.lower() == '':
            name = 'Hardware Diagnostic Sensor'
        elif name.lower() == '':
            name = 'Ion Distributor'
        elif name.lower() == 'sistemas de enriquecimiento terrestre':
            name = 'Land Enrichment Systems'
        elif name.lower() == 'equipamiento de diagnóstico medico':
            name = 'Medical Diagnostic Equipment'
        elif name.lower() == '':
            name = 'Micro Controllers'
        elif name.lower() == '':
            name = 'Muon Imager'
        elif name.lower() == '':
            name = 'Nanobreakers'
        elif name.lower() == 'separadores de resonancia':
            name = 'Resonating Separators'
        elif name.lower() == 'robots':
            name = 'Robotics'
        elif name.lower() == 'reguladores estructurales':
            name = 'Structural Regulators'
        elif name.lower() =='':
            name = 'Telemetry Suite'
        elif name.lower() == '':
            name = 'Conductive Fabrics'
        elif name.lower() == 'cuero':
            name = 'Leather'
        elif name.lower() == '':
            name = 'Military Grade Fabrics'
        elif name.lower() == '':
            name = 'Natural Fabrics'
        elif name.lower() == '':
            name = 'Synthetic Fabrics'
        elif name.lower() == 'residuos biológicos':
            name = 'Biowaste'
        elif name.lower() == 'residuos químicos':
            name = 'Chemical Waste'
        elif name.lower() == 'basura':
            name = 'Scrap'
        elif name.lower() == 'residuos tóxicos':
            name = 'Toxic Waste'
        elif name.lower() == 'armas de batalla':
            name = 'Battle Weapons'
        elif name.lower() == 'minas de superficie':
            name = 'Landmines'
        elif name.lower() == 'armas no letales':
            name = 'Non-lethal Weapons'
        elif name.lower() == 'armas personales':
            name = 'Personal Weapons'
        elif name.lower() == 'armadura reactiva':
            name = 'Reactive Armour'
        name = name.title()
        a = db.productos.find_one({'name': name})
        if a:
            name1 = m.text
            name2 = name1.title()
            e = a.get('is_rare')
            if e == 0:
                y = "No"
            else:
                y = "Sí"
            consulta = "*Nombre del producto*: {}\n*Categoría del Producto*: {}\n*Precio Medio del Producto*: {} Cr\n*Objeto Raro*: {} ".format(
            str(name2),
            a.get('category').get('name'),
            a.get('average_price'),
            str(y)
            )
        else:
            consulta = "Me da que ese producto no existe, Si crees que este objeto que has buscado existe y esta bien escrito pongase en contacto con nosotros usando /contactar"

    else:
        consulta = "Macho, pon el nombre"
    bot.send_message(cid, consulta, parse_mode="Markdown")
